from byte import Byte


class PBKD:

    @staticmethod
    def generate_key(salt=None, message='', iteration_count=1):
        if salt is None:
            salt = PBKD.get_salt()

        result = PBKD.HMAC(salt, message)
        for i in range(iteration_count - 1):
            temp = PBKD.HMAC(result, message)
            result = Byte.xor(result, temp)

        return result

    @staticmethod
    def HMAC(secret, message):
        """
        For hashes using HMAC SHA256 I convert java to python by using this link:
        http://jokecamp.wordpress.com/2012/10/21/examples-of-creating-base64-hashes-using-hmac-sha256-in-different-languages/#python

        keySpec = SecretKeySpec(key, "HmacSHA256")#javax.crypto.spec
        mac = Mac.getInstance("HmacSHA256")#javax.crypto.mac
        """
        import hashlib
        import hmac

        signature = hmac.new(secret, message, digestmod=hashlib.sha256).digest()
        
        return signature

    @staticmethod
    def __get_salt():
        return Byte.hex_to_byte("633f7b241f16d678c20f84e92d9197f1")
