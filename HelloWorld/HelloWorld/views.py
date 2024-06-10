from django.shortcuts import render

def index(request):
    # 變數
    context = {}
    context['name'] = "KageRyo"
    # 列表
    views_list = ["早安", "午安", "晚安"]
    context['views_list'] = views_list
    # 字典
    views_dict = {"name": "KageRyo", "age": 21, "school": "NUTC"}
    context['views_dict'] = views_dict
    # 判斷式
    score = 99
    context['score'] = score
    # 空列表
    empty_list = []
    context['empty_list'] = empty_list
    # 回傳渲染到index.html上
    return render(request, 'index.html', context)

def index1(request):
    context = {}
    context['name'] = "KageRyo"
    return render(request, 'index1.html', context)