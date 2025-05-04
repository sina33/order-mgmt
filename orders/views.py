from rest_framework import viewsets, filters, permissions
from .models import Order
from .serializers import OrderSerializer
from .permissions import IsAdminOrOwner

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrOwner]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['sum_price', 'created_at']
    search_fields = ['product_name']

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Order.objects.all()
        return Order.objects.filter(customer=user)

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)
