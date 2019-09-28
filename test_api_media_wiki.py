from GrandPy_BotApp.media_wiki_handler import MediaWikiHandler


def test_api_media_wiki(monkeypatch):
    """ test media wiki API  """

    result = 2
    #result = [('Hôtel de ville de Paris', 'L’hôtel de ville de Paris, communément appellé l’Hôtel de Ville, est le bâtiment qui héberge les institutions municipales de Paris depuis 1357.', 'https://fr.wikipedia.org/wiki/H%C3%B4tel_de_ville_de_Paris')]


    def mockreturn(request):
        return result

    monkeypatch.setattr('GrandPy_BotApp.media_wiki_handler.MediaWikiHandler.story_about_place.api_json_file', mockreturn)

    api = MediaWikiHandler()

    assert api.story_about_place() == result
