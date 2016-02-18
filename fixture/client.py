from apps.core.models import Client



def gen_client():
    Client.objects.create(first_name="Ana", last_name="Maria", phone="6432846659", cell="6899481612", address="rua pedro galvão", city="São Paulo", zip_code="54897965", state="SP", cpf="12546598563")
    Client.objects.create(first_name="Isabella", last_name="Pereira", phone="6432844456", cell="6899488288", address="rua maria antonieta", city="São Paulo", zip_code="21022154", state="SP", cpf="13659847846")
    Client.objects.create(first_name="Renato", last_name="Costa", phone="6432847777", cell="6899487852", address="rua da amargura", city="Rondonopolis", zip_code="10215654", state="MT", cpf="54565234581")
    Client.objects.create(first_name="Carolina", last_name="Souza", phone="6432840578", cell="6899487450", address="rua são joão", city="Manaus", zip_code="45879563", state="AM", cpf="20150543045")
    Client.objects.create(first_name="Marcela", last_name="Freitas", phone="6432840105", cell="6899481204", address="rua pedro oliveira", city="São Paulo", zip_code="30205456", state="SP", cpf="20215487895")
    Client.objects.create(first_name="Rafaela", last_name="Barros", phone="6432844042", cell="6899484578", address="rua das flores", city="São Paulo", zip_code="20021546", state="SP", cpf="20121564986")
    Client.objects.create(first_name="Luisa", last_name="Mendes", phone="6432841245", cell="6899484568", address="avenida dos andrades", city="Goiânia", zip_code="31356489", state="GO", cpf="21021505487")
    Client.objects.create(first_name="Gilson", last_name="Santos", phone="6432846482", cell="6899483154", address="avenida dos afonsos", city="São Paulo", zip_code="54689763", state="SP", cpf="32025015468")
    Client.objects.create(first_name="Roberto", last_name="Louro", phone="643284675", cell="6899486766", address="rua cristal", city="Macapá", zip_code="75849381", state="AP", cpf="30251505468")
    Client.objects.create(first_name="Maria", last_name="Nascimento", phone="643284456", cell="6899482143", address="rua dom abel", city="Fortaleza", zip_code="15634568", state="CE", cpf="23650546699")
    Client.objects.create(first_name="Roberta", last_name="Oliveira", phone="6432846598", cell="6894581613", address="rua rafael barbosa", city="Goiânia", zip_code="457867454", state="GO", cpf="524565458698")

gen_client()