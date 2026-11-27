---
declaration: theorem
origin: cited
lean: CohenLenstraHeuristics.cohen_lenstra_imaginary_quadratic_p_sylow_conjecture, CohenLenstraHeuristics.cohen_lenstra_real_quadratic_p_sylow_conjecture
statement: formalized
---

# Cohen–Lenstra Heuristics for Quadratic Class Groups

> Henri Cohen and Hendrik W. Lenstra Jr. [CL84, Co93] formulated probabilistic heuristics for the
> odd part of the ideal class group $\operatorname{Cl}(\mathcal{O}_{\mathbb{Q}(\sqrt{d})})$ as
> $\mathbb{Q}(\sqrt{d})$ varies over imaginary ($d < 0$) or real ($d > 0$) quadratic fields ordered
> by absolute fundamental discriminant $|D(d)|$.
>
> For an odd prime $p$ and a finite abelian $p$-group $G$, the heuristic at unit rank $u$ ($u = 0$
> when $d < 0$, $u = 1$ when $d > 0$) predicts that the proportion of quadratic fields whose
> $p$-Sylow class-group subgroup is isomorphic to $G$ converges to
>
> $$w_{p, u}(G) =
>   \frac{\prod_{k=1}^\infty \left(1 - p^{-(k + u)}\right)}{|G|^u \cdot |\operatorname{Aut}(G)|}.$$
>
> The cited Wikipedia section mentions only that these heuristics exist and quotes their $\approx
> 75.45\%$ class-number-$1$ prediction for prime-radicand real quadratic fields; the explicit odd
> $p$-part formulas formalized below come from [CL84] and [Co93, §5.10].
>
> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Class_number_problem#Real_quadratic_fields)
> - [CL84] H. Cohen and H. W. Lenstra Jr. (1984), Lecture Notes in Math. **1068**, Springer, 33–62.
> - [Co93] H. Cohen (1993), Grad. Texts in Math. **138**, Springer, §5.10.

*Quoted from [FormalConjectures/Wikipedia/CohenLenstraHeuristics.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/CohenLenstraHeuristics.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 2 test statements and 1 API statement, counted here but not shown.

## `CohenLenstraHeuristics.cohen_lenstra_imaginary_quadratic_p_sylow_conjecture`

Open: stated without proof.

> **Cohen–Lenstra Heuristic (Imaginary Quadratic Case, $u = 0$)** [CL84; Co93, §5.10]: given an
> odd prime $p$ and finite abelian $p$-group $G$, the fraction of imaginary quadratic discriminants
> $|D(d)| \le X$ whose $p$-Sylow class-group subgroup is isomorphic to $G$ tends to
> `cohenLenstraWeight p 0 G`. (Wikipedia notes only the existence of the heuristics and their
> $\approx 75.45\%$ real-quadratic prediction; this odd-$p$-part formula comes from [CL84] and
> [Co93, §5.10].)

```lean
theorem cohen_lenstra_imaginary_quadratic_p_sylow_conjecture (p : ℕ) [Fact p.Prime] (hp : p ≠ 2)
    (G : Type*) [CommGroup G] [Fintype G] (hG : IsPGroup p G) :
    Filter.Tendsto
      (fun X : ℕ =>
        (((imagQuadRadicandsUpTo X).filter (HasQuadPSylowIso p G)).card : ℝ) /
          ((imagQuadRadicandsUpTo X).card : ℝ))
      Filter.atTop (nhds (cohenLenstraWeight p 0 G))
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/CohenLenstraHeuristics.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/CohenLenstraHeuristics.lean#L83).

## `CohenLenstraHeuristics.cohen_lenstra_real_quadratic_p_sylow_conjecture`

Open: stated without proof.

> **Cohen–Lenstra Heuristic (Real Quadratic Case, $u = 1$)** [CL84; Co93, §5.10]: given an odd
> prime $p$ and finite abelian $p$-group $G$, the fraction of real quadratic discriminants
> $0 < D(d) \le X$ whose $p$-Sylow class-group subgroup is isomorphic to $G$ tends to
> `cohenLenstraWeight p 1 G`. (Wikipedia notes only the existence of the heuristics and their
> $\approx 75.45\%$ prediction; this odd-$p$-part formula comes from [CL84] and [Co93, §5.10].)

```lean
theorem cohen_lenstra_real_quadratic_p_sylow_conjecture (p : ℕ) [Fact p.Prime] (hp : p ≠ 2)
    (G : Type*) [CommGroup G] [Fintype G] (hG : IsPGroup p G) :
    Filter.Tendsto
      (fun X : ℕ =>
        (((realQuadRadicandsUpTo X).filter (HasQuadPSylowIso p G)).card : ℝ) /
          ((realQuadRadicandsUpTo X).card : ℝ))
      Filter.atTop (nhds (cohenLenstraWeight p 1 G))
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/CohenLenstraHeuristics.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/CohenLenstraHeuristics.lean#L99).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/CohenLenstraHeuristics.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/CohenLenstraHeuristics.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Class_number_problem#Real_quadratic_fields)
