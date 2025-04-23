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
    

def yu_gi_oh_calculator(request):
    # valores padão
    context = {
        'deck_size': 40,
        'copias_no_deck': 3,
        'mao_inicial': 5,
        'copias_desejadas': 1,
        'show_results': False
    } 
    
    if request.method == 'POST':
        try:
            #obtém valores do formulario
            N = int(request.POST.get('deck_size', 40))
            K = int(request.POST.get('copias_no_deck', 3))
            n = int(request.POST.get('mao_inicial', 5))
            k = int(request.POST.get('copias_desejadas', 1))
            
            #validação
            if K > N or k > n or any (val <= 0 for val in [N, K, n, k]):
                raise ValueError("Valores invalidos")

            # Calculo das probabilidades
            prob_exact, prob_at_least = hipergeometric_probability(N, K, n, k)

            # atualiza o contexto com resultado
            context.update({
                'deck_size': N,
                'copias_no_deck': K,
                'mao_inicial': n,
                'copias_desejadas': k,
                'prob_exact': f"{prob_exact * 100:.2f}%",
                'prob_at_least': f"{prob_at_least * 100:.2f}%",
                'show_results': True
            })
            
        except Exception as e:
            context['error'] = "por favor, insira valores válidos"
            
    return render(request, 'yugioh_prob/calculadora.html', context)