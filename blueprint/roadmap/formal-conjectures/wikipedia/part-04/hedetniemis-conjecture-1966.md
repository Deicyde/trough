---
declaration: theorem
origin: cited
lean: HedetniemiConjecture.hedetniemi_conjecture, HedetniemiConjecture.hedetniemi_conjecture.variants.el_zahar_sauer, HedetniemiConjecture.hedetniemi_conjecture.variants.shitov
statement: formalized
---

# Hedetniemi's conjecture (1966)

> *References:*
> * [Wikipedia](https://en.wikipedia.org/wiki/Hedetniemi%27s_conjecture)
> * [He66] Hedetniemi, S. T. (1966). *Homomorphisms of graphs and automata.* Technical Report
>   03105-44-T, University of Michigan.
> * [ES85] El-Zahar, M. and Sauer, N. (1985). "The chromatic number of the product of two
>   4-chromatic graphs is 4." *Combinatorica* 5, pp. 121--126.
> * [Sh19] Shitov, Y. (2019). "Counterexamples to Hedetniemi's conjecture." *Ann. of Math.* 190,
>   pp. 663--667. [arXiv:1905.02167](https://arxiv.org/abs/1905.02167)
> * [Ta22] Tardif, C. (2022). "The chromatic number of the product of 14-chromatic graphs can
>   be 13." *Combinatorica* 42, pp. 301--308.
> * [Zh21] Zhu, X. (2021). "Relatively small counterexamples to Hedetniemi's conjecture."
>   *J. Combin. Theory Ser. B* 146, pp. 141--150.

*Quoted from [FormalConjectures/Wikipedia/HedetniemiConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/HedetniemiConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 3 solved. It also has 1 API statement, counted here but not shown.

## `HedetniemiConjecture.hedetniemi_conjecture`

Solved: stated here without proof.

> **Hedetniemi's conjecture (1966) — disproved.**
>
> For all finite simple graphs $G$ and $H$, the chromatic number of the tensor product was
> conjectured to satisfy $\chi(G \times H) = \min\{\chi(G), \chi(H)\}$.
>
> This is **false**: Shitov [Sh19] constructed finite graphs $G$, $H$ with
> $\chi(G \times H) < \min\{\chi(G), \chi(H)\}$. The inequality $\le$ always holds
> (`chromaticNumber_tensorProd_le_min`); it is the reverse inequality that fails.

```lean
theorem hedetniemi_conjecture : ¬
    ∀ {α β : Type} [Fintype α] [Fintype β] (G : SimpleGraph α) (H : SimpleGraph β),
      (tensorProd G H).chromaticNumber = min G.chromaticNumber H.chromaticNumber
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/HedetniemiConjecture.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/HedetniemiConjecture.lean#L72).

## `HedetniemiConjecture.hedetniemi_conjecture.variants.el_zahar_sauer`

Solved: stated here without proof.

> **El-Zahar–Sauer (1985): the conjecture holds when `min {χ(G), χ(H)} ≤ 4`.**
>
> If both $G$ and $H$ are $4$-chromatic then so is $G \times H$; together with the easy cases
> $\min\{\chi(G), \chi(H)\} \le 3$, this gives Hedetniemi's equality whenever
> $\min\{\chi(G), \chi(H)\} \le 4$.
>
> *Reference:* [ES85].

```lean
theorem hedetniemi_conjecture.variants.el_zahar_sauer
    {α β : Type} [Fintype α] [Fintype β] (G : SimpleGraph α) (H : SimpleGraph β)
    (h : min G.chromaticNumber H.chromaticNumber ≤ 4) :
    (tensorProd G H).chromaticNumber = min G.chromaticNumber H.chromaticNumber
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/HedetniemiConjecture.lean, line 100](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/HedetniemiConjecture.lean#L100).

## `HedetniemiConjecture.hedetniemi_conjecture.variants.shitov`

Solved: stated here without proof.

> **Shitov (2019): the conjecture fails.**
>
> There exist finite graphs $G$, $H$ with $\chi(G \times H) < \min\{\chi(G), \chi(H)\}$.
> Tardif [Ta22] later gave counterexamples with $\min\{\chi(G),\chi(H)\} = 14$ and
> $\chi(G \times H) = 13$, and Zhu [Zh21] considerably smaller ones.
>
> *References:* [Sh19], [Ta22], [Zh21].

```lean
theorem hedetniemi_conjecture.variants.shitov :
    ∃ (α β : Type) (_ : Fintype α) (_ : Fintype β) (G : SimpleGraph α) (H : SimpleGraph β),
      (tensorProd G H).chromaticNumber < min G.chromaticNumber H.chromaticNumber
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/HedetniemiConjecture.lean, line 116](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/HedetniemiConjecture.lean#L116).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/HedetniemiConjecture.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/HedetniemiConjecture.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Hedetniemi%27s_conjecture)
