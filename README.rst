***************
Wagtail Metrics
***************

Wagtail Metrics allows you to retrieve information about Wagtail pages.

Information providers for Wagtail pages are :

- **wagtail_page** : retrieves all fields and blocks
- **request** : get the HTTP status code of Wagtail pages
- **google_page_speed** : collects scores on performance, accessibility, best practices and SEO

Usage
#####

You can use Wagtail Metric like this :

.. code-block:: python

    from wagtail.core.models import Site
    from wagtail_metrics.checkup import Checkup

    checkup = Checkup(providers=[
            'wagtail_page',
            'request',
            'google_page_speed'
    ])
    for site in Site.objects.all():
        checkup.add_site(site)
    checkup_json = self.checkup.to_json()

**checkup_json** is equal to :

.. code-block::

    {
        "stream_field__block__title": {
            "counter": 3,
            "values": {
                "generic title": {
                    "counter": 3,
                    "pages": [
                        "https://www.snoweb.io/fr/",
                        "https://www.snoweb.io/fr/cms/",
                        "https://www.snoweb.io/fr/cms/wagtail/"
                    ]
                }
            }
        },
        "stream_field__block__description": {
            "counter": 3,
            "values": {
                "different description 1": {
                    "counter": 1,
                    "pages": [
                        "https://www.snoweb.io/fr/"
                    ]
                },
                "different description 2": {
                    "counter": 1,
                    "pages": [
                        "https://www.snoweb.io/fr/cms/"
                    ]
                },
                "different description 3": {
                    "counter": 1,
                    "pages": [
                        "https://www.snoweb.io/fr/cms/wagtail/"
                    ]
                }
            }
        },
        "locale": {
            "counter": 3,
            "values": {
                "french": {
                    "counter": 3,
                    "pages": [
                        "https://www.snoweb.io/fr/",
                        "https://www.snoweb.io/fr/cms/",
                        "https://www.snoweb.io/fr/cms/wagtail/"
                    ]
                }
            }
        },
        "title": {
            "counter": 3,
            "values": {
                "Home": {
                    "counter": 1,
                    "pages": [
                        "https://www.snoweb.io/fr/"
                    ]
                },
                "CMS": {
                    "counter": 1,
                    "pages": [
                        "https://www.snoweb.io/fr/cms/"
                    ]
                },
                "Wagtail": {
                    "counter": 1,
                    "pages": [
                        "https://www.snoweb.io/fr/cms/wagtail/"
                    ]
                }
            }
        },
        "slug": {
            "counter": 3,
            "values": {
                "home": {
                    "counter": 1,
                    "pages": [
                        "https://www.snoweb.io/fr/"
                    ]
                },
                "cms": {
                    "counter": 1,
                    "pages": [
                        "https://www.snoweb.io/fr/cms/"
                    ]
                },
                "wagtail": {
                    "counter": 1,
                    "pages": [
                        "https://www.snoweb.io/fr/cms/wagtail/"
                    ]
                }
            }
        },
        "live": {
            "counter": 3,
            "values": {
                "true": {
                    "counter": 3,
                    "pages": [
                        "https://www.snoweb.io/fr/",
                        "https://www.snoweb.io/fr/cms/",
                        "https://www.snoweb.io/fr/cms/wagtail/"
                    ]
                }
            }
        },
        "owner": {
            "counter": 3,
            "values": {
                "none": {
                    "counter": 3,
                    "pages": [
                        "https://www.snoweb.io/fr/",
                        "https://www.snoweb.io/fr/cms/",
                        "https://www.snoweb.io/fr/cms/wagtail/"
                    ]
                }
            }
        },
        "seo_title": {
            "counter": 3,
            "values": {
                "": {
                    "counter": 3,
                    "pages": [
                        "https://www.snoweb.io/fr/",
                        "https://www.snoweb.io/fr/cms/",
                        "https://www.snoweb.io/fr/cms/wagtail/"
                    ]
                }
            }
        },
        "show_in_menus": {
            "counter": 3,
            "values": {
                "false": {
                    "counter": 3,
                    "pages": [
                        "https://www.snoweb.io/fr/",
                        "https://www.snoweb.io/fr/cms/",
                        "https://www.snoweb.io/fr/cms/wagtail/"
                    ]
                }
            }
        },
        "search_description": {
            "counter": 3,
            "values": {
                "": {
                    "counter": 3,
                    "pages": [
                        "https://www.snoweb.io/fr/",
                        "https://www.snoweb.io/fr/cms/",
                        "https://www.snoweb.io/fr/cms/wagtail/"
                    ]
                }
            }
        },
        "first_published_at": {
            "counter": 3,
            "values": {
                "none": {
                    "counter": 3,
                    "pages": [
                        "https://www.snoweb.io/fr/",
                        "https://www.snoweb.io/fr/cms/",
                        "https://www.snoweb.io/fr/cms/wagtail/"
                    ]
                }
            }
        },
        "last_published_at": {
            "counter": 3,
            "values": {
                "none": {
                    "counter": 3,
                    "pages": [
                        "https://www.snoweb.io/fr/",
                        "https://www.snoweb.io/fr/cms/",
                        "https://www.snoweb.io/fr/cms/wagtail/"
                    ]
                }
            }
        },
        "char_field": {
            "counter": 3,
            "values": {
                "Test char field": {
                    "counter": 3,
                    "pages": [
                        "https://www.snoweb.io/fr/",
                        "https://www.snoweb.io/fr/cms/",
                        "https://www.snoweb.io/fr/cms/wagtail/"
                    ]
                }
            }
        },
        "request__status_code": {
            "counter": 3,
            "values": {
                "200": {
                    "counter": 3,
                    "pages": [
                        "https://www.snoweb.io/fr/",
                        "https://www.snoweb.io/fr/cms/",
                        "https://www.snoweb.io/fr/cms/wagtail/"
                    ]
                }
            }
        },
        "google_page_speed__performance": {
            "counter": 3,
            "values": {
                "99": {
                    "counter": 1,
                    "pages": [
                        "https://www.snoweb.io/fr/"
                    ]
                },
                "84": {
                    "counter": 1,
                    "pages": [
                        "https://www.snoweb.io/fr/cms/"
                    ]
                },
                "75": {
                    "counter": 1,
                    "pages": [
                        "https://www.snoweb.io/fr/cms/wagtail/"
                    ]
                }
            }
        },
        "google_page_speed__accessibility": {
            "counter": 3,
            "values": {
                "95": {
                    "counter": 3,
                    "pages": [
                        "https://www.snoweb.io/fr/",
                        "https://www.snoweb.io/fr/cms/",
                        "https://www.snoweb.io/fr/cms/wagtail/"
                    ]
                }
            }
        },
        "google_page_speed__best_practices": {
            "counter": 3,
            "values": {
                "100": {
                    "counter": 3,
                    "pages": [
                        "https://www.snoweb.io/fr/",
                        "https://www.snoweb.io/fr/cms/",
                        "https://www.snoweb.io/fr/cms/wagtail/"
                    ]
                }
            }
        },
        "google_page__speed_seo": {
            "counter": 3,
            "values": {
                "100": {
                    "counter": 3,
                    "pages": [
                        "https://www.snoweb.io/fr/",
                        "https://www.snoweb.io/fr/cms/",
                        "https://www.snoweb.io/fr/cms/wagtail/"
                    ]
                }
            }
        },
        "stream_field__block_never_used__title": {
            "counter": 0,
            "values": {}
        }
    }

Setup
#####

Install with pip :

.. code-block::

    pip install wagtail_metrics

Set if needed in Django settings :

.. code-block::

    # Default value
    WAGTAIL_METRICS_DEFAULT_EXCLUDE = [
        'sites_rooted_here',
        'aliases',
        'revisions',
        'group_permissions',
        'view_restrictions',
        'workflow_states',
        'wagtail_admin_comments',
        'subscribers',
        'id',
        'path',
        'depth',
        'numchild',
        'translation_key',
        'draft_title',
        'has_unpublished_changes',
        'url_path',
        'go_live_at',
        'expire_at',
        'expired',
        'locked',
        'locked_at',
        'locked_by',
        'latest_revision_created_at',
        'live_revision',
        'alias_of',
        'page_ptr',
        'index_entries',
        'content_type'
    ]
    WAGTAIL_METRICS_INDENT_JSON = 4
    # For Google page speed
    WAGTAIL_METRICS_GOOGLE_API_KEY = 'xxx'
