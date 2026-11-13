---
declaration: theorem
origin: cited
lean: Erdos191.erdos_191, Erdos191.erdos_191.variants.conlon_fox_sudakov, Erdos191.erdos_191.variants.rodl_upper, Erdos191.erdos_191.variants.three_colours
statement: formalized
---

# Erdős Problem 191

> *References:*
> - [erdosproblems.com/191](https://www.erdosproblems.com/191)
> - [ErGr79] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory: van der Waerden's theorem and related topics*. Enseign. Math. (1979), 325-344.
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathematique (1980).
> - [Er81] Erdős, P., *On the combinatorial problems which I would most like to see solved*.
>   Combinatorica (1981), 25-42.
> - [Er82e] Erdős, Paul, *Some of my favourite problems which recently have been solved*. (1982),
>   59--79.
> - [Ro03] Rödl, Vojtěch, *On homogeneous sets of positive integers*. J. Combin. Theory Ser. A
>   (2003), 229-240.
> - [CFS13] Conlon, David and Fox, Jacob and Sudakov, Benny, *Two extensions of Ramsey's theorem*.
>   Duke Math. J. (2013), 2903-2927.

*Quoted from [FormalConjectures/ErdosProblems/191.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/191.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/191](https://www.erdosproblems.com/191).

The file states 4 research or textbook statements: 4 solved.

## `Erdos191.erdos_191`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos191.lean#L1272](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos191.lean#L1272).

> Let $C>0$ be arbitrary. Is it true that, if $n$ is sufficiently large depending on $C$, then in
> any $2$-colouring of $\binom{\{2,\ldots,n\}}{2}$ there exists some $X\subseteq \{2,\ldots,n\}$
> such that $\binom{X}{2}$ is monochromatic and
>
> $$\sum_{x\in X}\frac{1}{\log x}\geq C?$$
>
> The answer is yes, which was proved by Rödl [Ro03]. In the same article Rödl also proved a lower
> bound for this problem, constructing, for all $n$, a $2$-colouring of $\binom{\{2,\ldots,n\}}{2}$
> such that if $X\subseteq \{2,\ldots,n\}$ is such that $\binom{X}{2}$ is monochromatic then
>
> $$\sum_{x\in X}\frac{1}{\log x}\ll \log\log\log n.$$
>
> In the same paper Rödl proves that the answer to the main problem is negative if we consider
> $3$-colourings.
>
> This bound is best possible, as proved by Conlon, Fox, and Sudakov [CFS13], who proved that, if
> $n$ is sufficiently large, then in any $2$-colouring of $\binom{\{2,\ldots,n\}}{2}$ there exists
> some $X\subseteq \{2,\ldots,n\}$ such that $\binom{X}{2}$ is monochromatic and
>
> $$\sum_{x\in X}\frac{1}{\log x}\geq 2^{-8}\log\log\log n.$$
>
> A $2$-colouring of the pairs of $\{2,\ldots,n\}$ is a graph `G` on this vertex set; a
> monochromatic set is a clique or an independent set of `G`.

```lean
theorem erdos_191 : ∀ C : ℝ, 0 < C → ∀ᶠ n : ℕ in atTop,
    ∀ G : SimpleGraph (Finset.Icc 2 n), ∃ X : Finset (Finset.Icc 2 n),
      (G.IsClique X ∨ G.IsIndepSet X) ∧ C ≤ ∑ x ∈ X, 1 / Real.log (x : ℕ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/191.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/191.lean#L69).

## `Erdos191.erdos_191.variants.conlon_fox_sudakov`

Solved: stated here without proof.

> Conlon, Fox, and Sudakov [CFS13] proved that, if $n$ is sufficiently large, then in any
> $2$-colouring of $\binom{\{2,\ldots,n\}}{2}$ there exists some $X\subseteq \{2,\ldots,n\}$ such
> that $\binom{X}{2}$ is monochromatic and
>
> $$\sum_{x\in X}\frac{1}{\log x}\geq 2^{-8}\log\log\log n.$$

```lean
theorem erdos_191.variants.conlon_fox_sudakov : ∀ᶠ n : ℕ in atTop,
    ∀ G : SimpleGraph (Finset.Icc 2 n), ∃ X : Finset (Finset.Icc 2 n),
      (G.IsClique X ∨ G.IsIndepSet X) ∧
        2 ^ (-8 : ℤ) * Real.log (Real.log (Real.log n)) ≤ ∑ x ∈ X, 1 / Real.log (x : ℕ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/191.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/191.lean#L81).

## `Erdos191.erdos_191.variants.rodl_upper`

Solved: stated here without proof.

> Rödl [Ro03] constructed, for all $n$, a $2$-colouring of $\binom{\{2,\ldots,n\}}{2}$ such that
> if $X\subseteq \{2,\ldots,n\}$ is such that $\binom{X}{2}$ is monochromatic then
>
> $$\sum_{x\in X}\frac{1}{\log x}\ll \log\log\log n.$$

```lean
theorem erdos_191.variants.rodl_upper : ∃ c : ℝ, ∀ᶠ n : ℕ in atTop,
    ∃ G : SimpleGraph (Finset.Icc 2 n), ∀ X : Finset (Finset.Icc 2 n),
      G.IsClique X ∨ G.IsIndepSet X →
        ∑ x ∈ X, 1 / Real.log (x : ℕ) ≤ c * Real.log (Real.log (Real.log n))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/191.lean, line 93](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/191.lean#L93).

## `Erdos191.erdos_191.variants.three_colours`

Solved: stated here without proof.

> Rödl [Ro03] proved that the answer to [erdős_191](https://www.erdosproblems.com/191) is negative
> if we consider $3$-colourings: there is a constant $C$ such that for every $n$ some $3$-colouring
> of $\binom{\{2,\ldots,n\}}{2}$ has $\sum_{x\in X}\frac{1}{\log x} < C$ for every monochromatic
> $X$.

```lean
theorem erdos_191.variants.three_colours : ∃ C : ℝ, ∀ n : ℕ,
    ∃ c : Sym2 (Finset.Icc 2 n) → Fin 3, ∀ X : Finset (Finset.Icc 2 n),
      (∃ i : Fin 3, ∀ x ∈ X, ∀ y ∈ X, x ≠ y → c s(x, y) = i) →
        ∑ x ∈ X, 1 / Real.log (x : ℕ) < C
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/191.lean, line 106](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/191.lean#L106).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/191.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/191.lean)
- [erdosproblems.com/191](https://www.erdosproblems.com/191)
