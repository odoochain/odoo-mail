{
    "name": "AF Mass Mailing Sender Logs",
    "summary": "This module adds logger in Email Marketing >> Mailing.",
    "version": "12.0.1.0.2",
    "category": "Email Marketing",
    "description": """
	 v12.0.0.1 AFC-2185 Added logger in Email Marketing >> Mailing.\n
	 v12.0.1.0.2 AFC-2185 Updated code for Logs.\n
	 v12.0.1.0.3 AFC-2864 Exposed the mass_mailing_id field to the link.tracker form view in order to make it easier to connect a tracked link with a mass mailing.\n
    """,
    "license": "AGPL-3",
    "maintainer": "Vertel AB",
    "author": "Vertel AB",
    "contributors": ["Vertel AB"],
    "depends": [
        "mass_mailing"
    ],
    "data": [
        'views/mass_mailing_views.xml',
        'views/link_tracker.xml',
    ],
    "auto_install": False,
    "installable": True,
}
