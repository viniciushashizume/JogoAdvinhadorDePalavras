from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from .utils import gerarFeedback, obterPalavraAleatoria

# Variável global para armazenar a palavra (apenas como exemplo)
palavra_atual = obterPalavraAleatoria()

def jogo_view(request):
    global palavra_atual

    if request.method == "POST":
        tentativa = request.POST.get("tentativa", "").strip().lower()
        if len(tentativa) != len(palavra_atual):
            return JsonResponse({"error": f"A palavra deve ter {len(palavra_atual)} letras."}, status=400)

        feedback = gerarFeedback(palavra_atual, tentativa)
        acertou = tentativa == palavra_atual

        if acertou:
            palavra_atual = obterPalavraAleatoria()  # Reinicia o jogo com uma nova palavra

        return JsonResponse({"feedback": feedback, "acertou": acertou})

    return render(request, "jogo/index.html")