import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(
            'analisis.log', mode='w', encoding='utf-8', delay=False
        ),
        logging.StreamHandler()
    ]
)
