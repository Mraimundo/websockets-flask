import uuid
import qrcode

class Pix:
  def __init__(self):
    pass

  def create_payment(self, base_dir=""):
    # Criar o pagamento na instituição bancária e obter o ID do pagamento
    bank_payment_id = str(uuid.uuid4())

    hash_payment = f"hash_payment_{bank_payment_id}"

    img = qrcode.make(hash_payment)

    # Salvar a imagem do QR code em um diretório específico
    img.save(f"{base_dir}static/img/qr_code_payment_{bank_payment_id}.png")

    return {
      "bank_payment_id": bank_payment_id,
      "qr_code_path": f"qr_code_payment_{bank_payment_id}"
    }