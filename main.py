import search

if __name__ == "__main__":
    keyword = input("请输入搜索的关键词：")
    print("========搜索中========")
    result_search = search.search_by_name(keyword)
    for i in range(0, len(result_search)):
        print(str(i + 1) + "：" + result_search[i][0])
    target_url_int = input("请输入您要查看的条目序号：")
    if target_url_int.isnumeric():
        print("========获取中========")
        target_url = result_search[int(target_url_int)-1][1]
        print(search.search_by_url(target_url))
    else:
        print("输入的参数有误")
        exit()
