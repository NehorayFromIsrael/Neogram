def Func(Json_Message):

    try:
        caption = Json_Message["caption"]
    except:
        pass
    try:
        file_id = ["photo", Json_Message["photo"][0]["file_id"],caption]
    except:
        try:
            file_id = ["file", Json_Message["document"]["file_id"],caption]
        except:
            try:
                file_id = ["video", Json_Message["video"]["file_id"], caption]
            except:
                try:
                    file_id = ["voice", Json_Message["voice"]["file_id"], caption]
                except:
                    return None
    return file_id


