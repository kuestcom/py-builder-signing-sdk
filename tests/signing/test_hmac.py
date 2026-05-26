from unittest import TestCase

from py_builder_signing_sdk.signing.hmac import build_hmac_signature


class TestHMAC(TestCase):
    def test_build_hmac_signature(self):
        signature = build_hmac_signature(
            "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=",
            "1000000",
            "test-sign",
            "/orders",
            '{"hash": "0x123"}',
        )
        self.assertIsNotNone(signature)
        self.assertEqual(
            signature,
            "ZwAdJKvoYRlEKDkNMwd5BuwNNtg93kNaR_oU2HrfVvc=",
        )

    def test_query_parameters_are_excluded_from_signature(self):
        path_signature = build_hmac_signature(
            "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=",
            "1000000",
            "test-sign",
            "/orders",
            '{"hash": "0x123"}',
        )
        query_signature = build_hmac_signature(
            "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=",
            "1000000",
            "test-sign",
            "/orders?market=condition",
            '{"hash": "0x123"}',
        )

        self.assertEqual(query_signature, path_signature)
