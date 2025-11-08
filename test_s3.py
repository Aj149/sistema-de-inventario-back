import boto3
from decouple import config
import io

print("--- INICIANDO PRUEBA MANUAL DE S3 ---")

# 1. Leemos las mismas variables que usa Django
try:
    AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = config("AWS_STORAGE_BUCKET_NAME")
    AWS_S3_REGION_NAME = config("AWS_S3_REGION_NAME", "us-east-2")

    if not AWS_ACCESS_KEY_ID:
        print("ERROR: No se encontró AWS_ACCESS_KEY_ID en el .env")
        exit()

    print(f"Bucket: {AWS_STORAGE_BUCKET_NAME}")
    print(f"Región: {AWS_S3_REGION_NAME}")

except Exception as e:
    print(f"ERROR: Fallo al leer el archivo .env con decouple. ¿Existe? {e}")
    exit()

# 2. Creamos un archivo de prueba en memoria
dummy_file_content = "¡Si puedes leer esto, S3 FUNCIONA!"
dummy_file = io.BytesIO(dummy_file_content.encode('utf-8'))
file_path_in_s3 = "test/django_test.txt" # Ruta de prueba

# 3. Intentamos conectarnos y subir el archivo
try:
    s3_client = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_S3_REGION_NAME
    )

    print(f"Intentando subir '{file_path_in_s3}' al bucket...")

    # 4. Esta es la operación que está fallando silenciosamente en Django
    s3_client.upload_fileobj(
            dummy_file,
            AWS_STORAGE_BUCKET_NAME,
            file_path_in_s3
            
        )

    print("\n" + "="*40)
    print(f"¡ÉXITO! El archivo se subió a S3.")
    print(f"URL: https://{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com/{file_path_in_s3}")
    print("="*40 + "\n")

except Exception as e:
    print("\n" + "!"*40)
    print("¡FALLÓ! ESTE ES TU VERDADERO ERROR:")
    print(e)
    print("!"*40 + "\n")