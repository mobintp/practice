from django.shortcuts import render
from django.http import Http404, HttpResponse


# Create your views here.
def index(request):
    return render(request, "sp1/index.html")


texts = [
    "Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet suscipit ratione laboriosam nobis accusamus quidem architecto perferendis porro! Maiores necessitatibus commodi enim quo aut corrupti aliquid numquam iste, neque eligendi doloremque dignissimos deleniti expedita error quod voluptatum saepe magnam fuga!",
    "Lorem ipsum dolor sit amet consectetur adipisicing elit. In, delectus corrupti doloribus iure dolor temporibus suscipit, reprehenderit cumque libero quos rem, dolorem ut earum! Delectus ex cumque alias temporibus similique.",
    "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Ea fugiat numquam reprehenderit ipsa ex deleniti illum vero ut, exercitationem eveniet, accusantium facilis, saepe repellendus quis!",
]


def section(request, num):
    if 1 <= num <= 3:
        return HttpResponse(texts[num - 1])
    else:
        raise Http404("No such section")
