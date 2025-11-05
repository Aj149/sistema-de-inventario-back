# common/migrations/0002_load_provincias_cantones.py

from django.db import migrations

# Esta es la lista completa de Provincias y sus Cantones
# (¡No la escribas a mano!)
PROVINCIAS_CANTONES = {
    'Azuay': ['Cuenca', 'Girón', 'Gualaceo', 'Nabón', 'Paute', 'Pucará', 'San Fernando', 'Santa Isabel', 'Sigsig', 'Oña', 'Chordeleg', 'El Pan', 'Sevilla de Oro', 'Guachapala', 'Camilo Ponce Enríquez'],
    'Bolívar': ['Guaranda', 'Chillanes', 'Chimbo', 'Echeandía', 'San Miguel', 'Caluma', 'Las Naves'],
    'Cañar': ['Azogues', 'Biblián', 'Cañar', 'La Troncal', 'El Tambo', 'Déleg', 'Suscal'],
    'Carchi': ['Tulcán', 'Bolívar', 'Espejo', 'Mira', 'Montúfar', 'San Pedro de Huaca'],
    'Chimborazo': ['Riobamba', 'Alausi', 'Colta', 'Chambo', 'Chunchi', 'Guamote', 'Guano', 'Pallatanga', 'Penipe', 'Cumandá'],
    'Cotopaxi': ['Latacunga', 'La Maná', 'Pangua', 'Pujilí', 'Salcedo', 'Saquisilí', 'Sigchos'],
    'El Oro': ['Machala', 'Arenillas', 'Atahualpa', 'Balsas', 'Chilla', 'El Guabo', 'Huaquillas', 'Marcabelí', 'Pasaje', 'Piñas', 'Portovelo', 'Santa Rosa', 'Zaruma', 'Las Lajas'],
    'Esmeraldas': ['Esmeraldas', 'Eloy Alfaro', 'Muisne', 'Quinindé', 'San Lorenzo', 'Atacames', 'Rioverde', 'La Concordia'],
    'Galápagos': ['San Cristóbal', 'Isabela', 'Santa Cruz'],
    'Guayas': ['Guayaquil', 'Alfredo Baquerizo Moreno (Juján)', 'Balao', 'Balzar', 'Colimes', 'Daule', 'Durán', 'El Empalme', 'El Triunfo', 'Milagro', 'Naranjal', 'Naranjito', 'Palestina', 'Pedro Carbo', 'Samborondón', 'Santa Lucía', 'Salitre (Urbina Jado)', 'San Jacinto de Yaguachi', 'Playas (General Villamil)', 'Simón Bolívar', 'Coronel Marcelino Maridueña', 'Lomas de Sargentillo', 'Nobol', 'General Antonio Elizalde (Bucay)', 'Isidro Ayora'],
    'Imbabura': ['Ibarra', 'Antonio Ante', 'Cotacachi', 'Otavalo', 'Pimampiro', 'San Miguel de Urcuquí'],
    'Loja': ['Loja', 'Calvas', 'Catamayo', 'Celica', 'Chaguarpamba', 'Espíndola', 'Gonzanamá', 'Macará', 'Paltas', 'Puyango', 'Saraguro', 'Sozoranga', 'Zapotillo', 'Pindal', 'Quilanga', 'Olmedo'],
    'Los Ríos': ['Babahoyo', 'Baba', 'Montalvo', 'Puebloviejo', 'Quevedo', 'Urdaneta', 'Ventanas', 'Vínces', 'Palenque', 'Buena Fe', 'Valencia', 'Mocache', 'Quinsaloma'],
    'Manabí': ['Portoviejo', 'Bolívar', 'Chone', 'El Carmen', 'Flavio Alfaro', 'Jipijapa', 'Junín', 'Manta', 'Montecristi', 'Paján', 'Pichincha', 'Rocafuerte', 'Santa Ana', 'Sucre', 'Tosagua', '24 de Mayo', 'Pedernales', 'Jama', 'Jaramijó', 'Puerto López', 'Olmedo', 'San Vicente'],
    'Morona Santiago': ['Morona', 'Gualaquiza', 'Limón Indanza', 'Palora', 'Santiago', 'Sucúa', 'Huamboya', 'San Juan Bosco', 'Taisha', 'Logroño', 'Pablo Sexto', 'Tiwintza'],
    'Napo': ['Tena', 'Archidona', 'El Chaco', 'Quijos', 'Carlos Julio Arosemena Tola'],
    'Orellana': ['Orellana (Francisco de Orellana)', 'Aguarico', 'La Joya de los Sachas', 'Loreto'],
    'Pastaza': ['Pastaza (Puyo)', 'Mera', 'Santa Clara', 'Arajuno'],
    'Pichincha': ['Quito', 'Cayambe', 'Mejía', 'Pedro Moncayo', 'Rumiñahui', 'San Miguel de los Bancos', 'Pedro Vicente Maldonado', 'Puerto Quito'],
    'Santa Elena': ['Santa Elena', 'La Libertad', 'Salinas'],
    'Santo Domingo de los Tsáchilas': ['Santo Domingo'],
    'Sucumbíos': ['Lago Agrio', 'Gonzalo Pizarro', 'Putumayo', 'Shushufindi', 'Sucumbíos', 'Cascales', 'Cuyabeno'],
    'Tungurahua': ['Ambato', 'Baños de Agua Santa', 'Cevallos', 'Mocha', 'Patate', 'Quero', 'San Pedro de Pelileo', 'Santiago de Píllaro', 'Tisaleo'],
    'Zamora Chinchipe': ['Zamora', 'Chinchipe', 'Nangaritza', 'Palanda', 'Yacuambi', 'Yantzaza (Yanzatza)', 'El Pangui', 'Centinela del Cóndor', 'Paquisha']
}


def load_data(apps, schema_editor):
    """
    Esta función se ejecutará cuando corras 'migrate'.
    Leerá el diccionario de arriba y creará los objetos en la BD.
    """
    # Obtenemos las versiones de los modelos de esta migración
    Provincia = apps.get_model('common', 'Provincia')
    Canton = apps.get_model('common', 'Canton') # Asumiendo que tu modelo se llama 'Canton' (singular)

    print("\n[INFO] Iniciando la carga de Provincias y Cantones...")

    # Usamos get_or_create para no duplicar si se corre de nuevo
    for prov_nombre, cantones_lista in PROVINCIAS_CANTONES.items():
        
        # 1. Crea la provincia
        prov_obj, created = Provincia.objects.get_or_create(nombre=prov_nombre)
        if created:
            print(f"  Provincia '{prov_nombre}' creada.")
            
        # 2. Crea los cantones para esa provincia
        for canton_nombre in cantones_lista:
            Canton.objects.get_or_create(nombre=canton_nombre, provincia=prov_obj)
            
    print("[INFO] Carga de datos completada.")


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),  # 👈 Cambia esto al nombre de tu migración ANTERIOR
    ]

    operations = [
        # Aquí le decimos a Django que ejecute nuestra función
        migrations.RunPython(load_data),
    ]