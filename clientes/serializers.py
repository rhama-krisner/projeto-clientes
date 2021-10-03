from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    
    def validate(self, data): #data, tem o acesso à todos os campos do serializer

        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':'CPF inválido'})
        
        if not nome_valido(data['nome']):
           raise serializers.ValidationError({'nome':'Não incluir números neste campo.'})

        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':'RG inválido'})

        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':'O numero de Celular deve seguir o padrão: xx 9xxxx-xxxx'})
        return data


    
    

     



