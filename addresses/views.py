from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from .models import Address, User
from .serializers import AddressSerializer

class AddressAll(APIView):
    def get(self, request):
        addresses = Address.objects.all()
        serializer = AddressSerializer(addresses, many=True)
        return Response(serializer.data)

class AddressUsers(APIView):
    def get_object(self, address_id):  ## get_object 는 특정 객체를 조회하거나 가져오는데 사용되는 메소드 /
        try:
            return Address.objects.get(id=address_id)
        except Address.DoesNotExist:
            raise NotFound
        
    def get(self, request, address_id):
        address = self.get_object(address_id=address_id)
        serializer = AddressSerializer(address)
        return Response(serializer.data)
    
class CreateUserAddress(APIView):
    def post(self, request, user_id):
        # user_id 검증
        user = User.objects.filter(id=user_id).first()  # 존재하지 않으면 None 반환
        if not user:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        # Address 생성
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)  # 외래 키로 User 객체를 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UpdateAddress(APIView):
    def get_object(self, address_id):  # get_object 메서드 추가
        try:
            return Address.objects.get(id=address_id)
        except Address.DoesNotExist:
            raise NotFound("Address not found")
    
    def put(self, request, address_id):
        address = self.get_object(address_id)
        serializer = AddressSerializer(address, data=request.data, partial=True)

        if serializer.is_valid():
            address = serializer.save()
            serializer = AddressSerializer(address)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class DeleteAddress(APIView):
    def get_object(self, address_id):
        try:
            return Address.objects.get(id=address_id)
        except Address.DoesNotExist:
            return None
        
    def delete(self, request, address_id):
        address = self.get_object(address_id)
        if address is None:
            return Response({'error': 'Address not found'}, status=status.HTTP_404_NOT_FOUND)
        address.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
