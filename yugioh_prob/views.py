from django.shortcuts import render
from math import comb
# Create your views here.


def hipergeometric_probability(N, K, n, k):
    """
    N = tamanho do deck
    K = cópias da carta no deck
    n = tamanho da mão
    k = cópias desejadas na mão
    """
    prob_exact = (comb(K, k) * comb(N - K, n - k)) / comb(N, n)
    prob_at_last = sum((comb(K,i) * comb(N - K,n - i)) / comb(N, n) for i in range(k,min(K,n) + 1))
    return prob_exact, prob_at_last
    

def calcular_probabilidade(request):
    if request.method == 'POST':
        N = int(request.POST.get('deck_size', 40))
        K = int(request.POST.get('copias_no_deck', 3))
        n = int(request.POST.get('mao_inicial', 5))
        k = int(request.POST.get('copias_desejadas', 1))
        
        if K > N or k > n or any (val <= 0 for val in [N,K,n,k]):
            raise ValueError("Valores inválidos")
        
        prob_exact, prob_at_least = hipergeometric_probability(N, K, n, k)
        
        return render(request, 'yugioh_prob/resultado.html', {
            'prob_exact': f"{prob_exact * 100:.2f}%",
            'prob_at_least': f"{prob_at_least * 100:.2f}%",
            'copias_desejadas': k,
        })
    return render(request, 'yugioh_prob/calcular.html')