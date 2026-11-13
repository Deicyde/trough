---
declaration: theorem
origin: cited
lean: Erdos90.erdos_90, Erdos90.erdos_90.variants.polynomial_lower_bound, Erdos90.erdos_90.variants.sawin_explicit, Erdos90.sawin_lattice_reduction, Erdos90.sawin_totally_real_tower
statement: formalized
---

# Erdős Problem 90: The unit distance problem

> *Reference:* [erdosproblems.com/90](https://www.erdosproblems.com/90)
>
> The conjecture asks whether every set of $n$ points in $\mathbb{R}^2$ determines at most
> $n^{1 + O(1/\log\log n)}$ unit distances. It was **disproved** in May 2026: an internal model at
> OpenAI produced a construction beating the conjectured bound, with the proof digested and
> human-verified in two arXiv papers:
>
> * W. Sawin, [*An explicit lower bound for the unit distance problem*](https://arxiv.org/abs/2605.20579)
>   (2026), giving $u(n) \ge n^{1.014114}/C$ for infinitely many $n$;
> * N. Alon, T. F. Bloom, W. T. Gowers, D. Litt, W. Sawin, A. Shankar, J. Tsimerman, V. Wang and
>   M. Matchett Wood, [*Remarks on the disproof of the unit distance conjecture*](https://arxiv.org/abs/2605.20695)
>   (2026), giving the qualitative form $u(n) \ge n^{1+\varepsilon}$ for some $\varepsilon > 0$.
>
> This file records the main statement (`erdos_90`), the two constructive disproof variants, the
> logical implications between them, and the load-bearing reductions of Sawin's proof
> (`sawin_lattice_reduction` and `sawin_totally_real_tower`) as further benchmark challenges.

*Quoted from [FormalConjectures/ErdosProblems/90.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/90.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/90](https://www.erdosproblems.com/90).

The file states 5 research or textbook statements: 5 solved. It also has 3 test statements, counted here but not shown.

## `Erdos90.erdos_90`

Solved: stated here without proof.

> Does every set of $n$ distinct points in $\mathbb{R}^2$ contain at most
> $n^{1+O(\frac{1}{\log\log n})}$ many pairs which are distance $1$ apart?
>
> This was
> [disproved](https://cdn.openai.com/pdf/74c24085-19b0-4534-9c90-465b8e29ad73/unit-distance-proof.pdf)
> by an internal model at OpenAI, which constructed (for infinitely many $n$) a set $P$ of $n$ points
> in $\mathbb{R}^2$ such that the number of unit distance pairs in $P$ is at least $n^{1+c}$, where
> $c > 0$ is an absolute constant.

```lean
theorem erdos_90 : ¬ ∃ (O : ℕ → ℝ) (hO : O =O[atTop] (fun n => 1 / (n : ℝ).log.log)),
    (fun n => (maxUnitDistances n : ℝ)) =ᶠ[atTop] fun (n : ℕ) => (n : ℝ) ^ (1 + O n)
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/90.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/90.lean#L86).

## `Erdos90.erdos_90.variants.polynomial_lower_bound`

Solved: stated here; a Lean proof is at [https://github.com/plby/Erdos90/blob/2062b0e6c9770c81e397bfe41148e90b92ca0567/src/submission/Solution.lean#L6](https://github.com/plby/Erdos90/blob/2062b0e6c9770c81e397bfe41148e90b92ca0567/src/submission/Solution.lean#L6).

> **Constructive form of the disproof.** There is an absolute constant $c > 0$ such that
> infinitely many $n$ admit a configuration realising at least $n^{1+c}$ unit distances.
>
> This is the qualitative content of Theorem 1.1 of Alon–Bloom–Gowers–Litt–Sawin–Shankar–
> Tsimerman–Wang–Matchett Wood, [*Remarks on the disproof of the unit distance conjecture*](https://arxiv.org/abs/2605.20695)
> (2026). An explicit bound $c \ge 0.014114$ is given by Sawin, [*An explicit lower bound for the
> unit distance problem*](https://arxiv.org/abs/2605.20579) (2026); see
> `erdos_90.variants.sawin_explicit` below.

```lean
theorem erdos_90.variants.polynomial_lower_bound :
    ∃ c > (0 : ℝ),
      {n : ℕ | (n : ℝ) ^ (1 + c) ≤ (maxUnitDistances n : ℝ)}.Infinite
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/90.lean, line 103](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/90.lean#L103).

## `Erdos90.erdos_90.variants.sawin_explicit`

Solved: stated here without proof.

> **Sawin's explicit exponent.** The constructive disproof can be realised with $c \ge 0.014114$
> (absorbing the implicit constant $C$ of Sawin's Theorem 1 into a slightly smaller exponent for
> all large enough $n$). Reference: Theorem 1 of Sawin, [arXiv:2605.20579](https://arxiv.org/abs/2605.20579)
> (2026).

```lean
theorem erdos_90.variants.sawin_explicit :
    {n : ℕ | (n : ℝ) ^ (1.014114 : ℝ) ≤ (maxUnitDistances n : ℝ)}.Infinite
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/90.lean, line 115](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/90.lean#L115).

## `Erdos90.sawin_lattice_reduction`

Solved: stated here without proof.

> **Sawin's Lemma 2: lattice geometry of unit distances** (Sawin, [arXiv:2605.20579](https://arxiv.org/abs/2605.20579)).
>
> Let $d \ge 1$, $R > 1$, and suppose $\Lambda \subset \mathbb{R}^{2d}$ is an additive subgroup
> all of whose nonzero vectors have norm at least $\rho > 0$ (so $\Lambda$ is a lattice; Sawin takes
> $\rho$ to be the norm of a shortest nonzero vector of $\Lambda$), equipped with an additive
> embedding $\pi : \Lambda \to \mathbb{R}^2$. Suppose $S \subseteq \Lambda$ is a finite set of
> "matching" vectors satisfying $\|v\| \le 1$ and $\|\pi v\| = 1$ for every $v \in S$. Then there
> is a finite point set $U \subset \mathbb{R}^2$ of size $\#U \le (2R/\rho + 1)^{2d}$ whose
> unit-distance density is at least $(1 - 1/R)^{2d}\,\#S$, i.e.
> $(1-1/R)^{2d}\,\#S\,\#U \le \#\{(u_1, u_2) \in U^2 : |u_1 - u_2| = 1\}$. The right-hand side
> counts ordered pairs, so it equals twice `unitDistNum U`.
>
> This pure geometry-of-numbers reduction is the elementary heart of the disproof.

```lean
theorem sawin_lattice_reduction
    (d : ℕ) (hd : 1 ≤ d) (R : ℝ) (hR : 1 < R)
    (Λ : Submodule ℤ (EuclideanSpace ℝ (Fin (2*d))))
    (ρ : ℝ) (hρ : 0 < ρ) (hΛ : ∀ v : Λ, v ≠ 0 → ρ ≤ ‖(v : EuclideanSpace ℝ (Fin (2*d)))‖)
    (π : Λ →+ ℝ²) (hπ : Function.Injective π)
    (S : Finset Λ)
    (hS_norm : ∀ v ∈ S, ‖(v : EuclideanSpace ℝ (Fin (2*d)))‖ ≤ 1)
    (hS_proj : ∀ v ∈ S, ‖π v‖ = 1) :
    ∃ U : Finset ℝ², 0 < U.card ∧ (U.card : ℝ) ≤ (2 * R / ρ + 1) ^ (2*d) ∧
      ((1 : ℝ) - 1/R) ^ (2*d) * (S.card : ℝ) * (U.card : ℝ) ≤
        2 * (unitDistNum U : ℝ)
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/90.lean, line 168](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/90.lean#L168).

## `Erdos90.sawin_totally_real_tower`

Solved: stated here; a Lean proof is at [https://github.com/n-yamaguchi-0729/SawinTotallyRealTowers/blob/3a455e1aa9140dbbe7b7d68f508392a69c86d0f4/Lean4/SawinTotallyRealTowers/SawinTotallyRealTower.lean#L31](https://github.com/n-yamaguchi-0729/SawinTotallyRealTowers/blob/3a455e1aa9140dbbe7b7d68f508392a69c86d0f4/Lean4/SawinTotallyRealTowers/SawinTotallyRealTower.lean#L31).

> **Sawin's Lemmas 11–12 / Remarks Proposition 2.3: the totally real tower.**
>
> There exist $rdBound : \mathbb{R}$ and a *single* infinite set $Q$ of rational primes
> $q \equiv 1 \pmod 4$ such that for every $N$ one can find a totally real number field $F/\mathbb{Q}$
> of degree $\ge N$ with bounded root discriminant $|disc F|^{1/[F:\mathbb{Q}]} \le rdBound$ in which
> *every* prime $q \in Q$ splits completely.
>
> The load-bearing feature is the quantifier order: $Q$ is fixed *before* $F$, so the same primes
> split completely in fields of *unbounded* degree. (For a single fixed $F$, Chebotarev already
> gives infinitely many completely split primes $\equiv 1 \pmod 4$, so a per-field statement would
> be vacuous.) This uniform splitting in an unbounded tower is the key arithmetic input to the
> disproof. It is proved as Lemmas 11–12 of Sawin, [arXiv:2605.20579](https://arxiv.org/abs/2605.20579),
> and as Proposition 2.3 of the [Remarks](https://arxiv.org/abs/2605.20695) paper, via the
> Golod–Shafarevich inequality for pro-$2$ groups together with the Hajir–Maire–Ramakrishna (2003)
> tower construction.
>
> A "completely split" rational prime $q$ in $F$ is one for which $(q)$ is the product of exactly
> $[F:\mathbb{Q}]$ distinct maximal ideals.

```lean
theorem sawin_totally_real_tower :
    ∃ (rdBound : ℝ) (Q : Set ℕ), Q.Infinite ∧ (∀ q ∈ Q, q.Prime ∧ q % 4 = 1) ∧
      ∀ N : ℕ, ∃ (F : Type) (_ : Field F) (_ : CharZero F) (_ : NumberField F)
        (_ : IsTotallyReal F),
        N ≤ Module.finrank ℚ F ∧
        (|(NumberField.discr F : ℝ)|) ^ ((1 : ℝ) / Module.finrank ℚ F) ≤ rdBound ∧
        ∀ q ∈ Q, ∃ (factors : Finset (Ideal (𝓞 F))),
          factors.card = Module.finrank ℚ F ∧
          ∀ p ∈ factors, p.IsMaximal ∧ (q : 𝓞 F) ∈ p
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/90.lean, line 204](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/90.lean#L204).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/90.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/90.lean)
- [erdosproblems.com/90](https://www.erdosproblems.com/90)
