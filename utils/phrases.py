
def prepare_phrases_for_processing(phrases):
    return {x['sequence']: x['phrases'] for x in phrases.values()}
