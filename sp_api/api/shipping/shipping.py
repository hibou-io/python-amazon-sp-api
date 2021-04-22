from sp_api.base.helpers import sp_endpoint, fill_query_params
from sp_api.base import Client, Marketplaces, deprecated, NotificationType, ApiResponse


class Shipping(Client):
    """
    :link: https://github.com/amzn/selling-partner-api-docs/blob/main/references/shipping-api/shipping.md
    """

    """
{
    "clientReferenceId": "p",
    "containers": [
        {
            "containerReferenceId": "cupidatat ",
            "dimensions": {
                "height": 37059838.611901075,
                "length": -7167684.493222252,
                "unit": "CM",
                "width": 31287817.198247537
            },
            "items": [
                {
                    "quantity": -19555878.11641468,
                    "title": "pariatur ",
                    "unitPrice": {
                        "unit": "ali",
                        "value": 56093445.451793045
                    },
                    "unitWeight": {
                        "unit": {
                            "value": "<Error: Too many levels of nesting to fake this schema>"
                        },
                        "value": {
                            "value": "<Error: Too many levels of nesting to fake this schema>"
                        }
                    }
                },
                {
                    "quantity": 8927757.590852886,
                    "title": "ea pro",
                    "unitPrice": {
                        "unit": "sit",
                        "value": -29950791.307383493
                    },
                    "unitWeight": {
                        "unit": {
                            "value": "<Error: Too many levels of nesting to fake this schema>"
                        },
                        "value": {
                            "value": "<Error: Too many levels of nesting to fake this schema>"
                        }
                    }
                }
            ],
            "value": {
                "unit": "pro",
                "value": 84288194.91332501
            },
            "weight": {
                "unit": {
                    "value": "<Error: Too many levels of nesting to fake this schema>"
                },
                "value": {
                    "value": "<Error: Too many levels of nesting to fake this schema>"
                }
            },
            "containerType": "PACKAGE"
        },
        {
            "containerReferenceId": "minim quis ullamco",
            "dimensions": {
                "height": -30009436.49445471,
                "length": -43075685.083735496,
                "unit": "IN",
                "width": -52323248.75380949
            },
            "items": [
                {
                    "quantity": 63215202.79483086,
                    "title": "ipsum tempor",
                    "unitPrice": {
                        "unit": "des",
                        "value": 21079653.490808383
                    },
                    "unitWeight": {
                        "unit": {
                            "value": "<Error: Too many levels of nesting to fake this schema>"
                        },
                        "value": {
                            "value": "<Error: Too many levels of nesting to fake this schema>"
                        }
                    }
                },
                {
                    "quantity": 39405732.81589335,
                    "title": "consectetur",
                    "unitPrice": {
                        "unit": "con",
                        "value": 51779910.17542899
                    },
                    "unitWeight": {
                        "unit": {
                            "value": "<Error: Too many levels of nesting to fake this schema>"
                        },
                        "value": {
                            "value": "<Error: Too many levels of nesting to fake this schema>"
                        }
                    }
                }
            ],
            "value": {
                "unit": "ame",
                "value": -11534125.751512602
            },
            "weight": {
                "unit": {
                    "value": "<Error: Too many levels of nesting to fake this schema>"
                },
                "value": {
                    "value": "<Error: Too many levels of nesting to fake this schema>"
                }
            },
            "containerType": "PACKAGE"
        }
    ],
    "labelSpecification": {
        "labelFormat": "PNG",
        "labelStockSize": "4x6"
    },
    "serviceType": "Amazon Shipping Ground",
    "shipFrom": {
        "addressLine1": "anim",
        "city": "proid",
        "countryCode": "su",
        "name": "aute",
        "postalCode": "ni",
        "stateOrRegion": "non ullamco magna in",
        "addressLine2": "sit ut cul",
        "addressLine3": "Duis pariatur",
        "email": "labore quis",
        "copyEmails": [
            "culpa in",
            "pariatur aute elit Excepteur"
        ],
        "phoneNumber": "officia in"
    },
    "shipTo": {
        "addressLine1": "Duis et",
        "city": "fugiat",
        "countryCode": "el",
        "name": "nostrud reprehende",
        "postalCode": "Lorem culpa ci",
        "stateOrRegion": "esse quis id fugiat nostrud",
        "addressLine2": "enim",
        "addressLine3": "sed ullamco qui tempor",
        "email": "est",
        "copyEmails": [
            "amet",
            "cupidatat"
        ],
        "phoneNumber": "Lo"
    },
    "shipDate": "1985-10-27T16:16:28.801Z"
}
    """

    @sp_endpoint('/shipping/v1/purchaseShipment', method='POST')
    def purchase_shipment(self, data, **kwargs) -> ApiResponse:
        # TODO why do they blend the kwargs in?
        return self._request(kwargs.pop('path'), data=data)

    """
    {
    "containerSpecifications": [
        {
            "dimensions": {
                "height": 55820746.24605319,
                "length": -17011895.59158598,
                "unit": "CM",
                "width": 92714119.67221498
            },
            "weight": {
                "unit": {
                    "value": "<Error: Too many levels of nesting to fake this schema>"
                },
                "value": {
                    "value": "<Error: Too many levels of nesting to fake this schema>"
                }
            }
        },
        {
            "dimensions": {
                "height": 52794069.63785118,
                "length": 38093725.6342161,
                "unit": "IN",
                "width": -69636208.8350734
            },
            "weight": {
                "unit": {
                    "value": "<Error: Too many levels of nesting to fake this schema>"
                },
                "value": {
                    "value": "<Error: Too many levels of nesting to fake this schema>"
                }
            }
        }
    ],
    "serviceTypes": [
        "Amazon Shipping Premium",
        "Amazon Shipping Ground"
    ],
    "shipFrom": {
        "addressLine1": "ad eu",
        "city": "id in cupidatat officia",
        "countryCode": "ex",
        "name": "consectetur",
        "postalCode": "com",
        "stateOrRegion": "laborum veniam",
        "addressLine2": "ex eu consectetur minim",
        "addressLine3": "deserunt incididunt nisi",
        "email": "culpa e",
        "copyEmails": [
            "deserunt Duis Except",
            "ad ex"
        ],
        "phoneNumber": "veniam in ir"
    },
    "shipTo": {
        "addressLine1": "cupidatat elit laborum",
        "city": "consectetur anim magna sint",
        "countryCode": "no",
        "name": "ad ",
        "postalCode": "culpa labore",
        "stateOrRegion": "labore laborum qui est",
        "addressLine2": "enim qui tempor deserunt ut",
        "addressLine3": "fugiat pariatur el",
        "email": "non",
        "copyEmails": [
            "aute adipisicing sunt",
            "nostru"
        ],
        "phoneNumber": "Duis ad ei"
    },
    "shipDate": "2001-05-19T22:20:47.778Z"
}
    """
    @sp_endpoint('/shipping/v1/rates', method='POST')
    def purchase_shipment(self, data, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), data=data)

    @sp_endpoint('/shipping/v1/account')
    def get_account(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), params={**kwargs})

    @sp_endpoint('/shipping/v1/tracking/{}')
    def get_tracking(self, tracking_id: str, **kwargs) -> ApiResponse:
        return self._request(fill_query_params(kwargs.pop('path'), tracking_id), params={**kwargs}
                             # TODO maybe? then clean these lines up!
                             # , add_marketplace=False
                             )
