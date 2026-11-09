---
declaration: theorem
origin: cited
lean: Green5.green_5, Green5.green_5.variants.kedlaya, Green5.green_5.variants.sl_two, Green5.green_5.variants.gowers_sl_two
statement: formalized
---

# Ben Green's Open Problem 5

> *References:*
> - [Gr24] [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.5)
> - [BaSo85] Babai L, Sós VT. Sidon sets in groups and induced subgraphs of Cayley graphs.
>   European Journal of Combinatorics. 1985 Jun 1;6(2):101-14.
> - [Ke97] Kedlaya, K. S., *Large product-free subsets of finite groups*, J. Combin. Theory
>   Ser. A 77 (1997), no. 2, 339–343.
> - [Ke09] Kedlaya, K. S., *Product-free subsets of groups, then and now*, Contemp. Math., 479,
>   American Mathematical Society, Providence, RI, 2009, 169–177.
> - [Go08] Gowers, W. T., *Quasirandom groups*, Combin. Probab. Comput. 17 (2008), no. 3,
>   363–387.

*Quoted from [FormalConjectures/GreensOpenProblems/5.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/5.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 2 open and 2 solved.

## `Green5.green_5`

Open: stated without proof.

> Which finite groups have the smallest biggest product-free sets?
>
> We formalise this as: determine the supremum of exponents $\alpha$ such that every nontrivial
> finite group of order $n$ contains a product-free set of size $\geq c n^{\alpha}$ for some
> absolute constant $c > 0$. (The trivial group is excluded since its only product-free subset
> is empty.) Kedlaya [Ke97] showed that $\alpha = 11/14$ is admissible, and Green suggests this
> exponent may well be sharp; the candidate extremal family is the Ree groups ${}^2G_2(q)$,
> $q = 3^{2m+1}$.

```lean
theorem green_5 :
    IsLUB {α : ℝ | ∃ c > (0 : ℝ), ∀ (G : Type) [Group G] [Fintype G], Nontrivial G →
      ∃ S : Finset G, IsProductFree (S : Set G) ∧
        c * (Fintype.card G : ℝ) ^ α ≤ (S.card : ℝ)}
      green_5.answer
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/GreensOpenProblems/5.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/5.lean#L56).

## `Green5.green_5.variants.kedlaya`

Solved: stated here without proof.

> Kedlaya [Ke97] observed, refining some work of Babai and Sós [BaSo85], that it follows from the
> classification of finite simple groups that every finite group $G$ of order $n$ has a
> product-free subset of size $\gg n^{11/14}$.

```lean
theorem green_5.variants.kedlaya :
    ∃ c > (0 : ℝ), ∀ (G : Type) [Group G] [Fintype G], Nontrivial G →
      ∃ S : Finset G, IsProductFree (S : Set G) ∧
        c * (Fintype.card G : ℝ) ^ ((11 : ℝ) / 14) ≤ (S.card : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/GreensOpenProblems/5.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/5.lean#L69).

## `Green5.green_5.variants.sl_two`

Open: stated without proof.

> A good model problem would be to determine the largest product-free subsets of
> $\mathrm{SL}_2(\mathbb{F}_p)$.

```lean
theorem green_5.variants.sl_two (p : ℕ) [Fact p.Prime] :
    let S : Finset (SL₂ p) := (green_5.variants.sl_two.answer p)
    MaximalFor (IsProductFree (M := SL₂ p)) Set.ncard (S : Set (SL₂ p))
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/GreensOpenProblems/5.lean, line 84](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/5.lean#L84).

## `Green5.green_5.variants.gowers_sl_two`

Solved: stated here without proof.

> For the largest product-free subsets of $\mathrm{SL}_2(\mathbb{F}_p)$ of order $n$, the
> best-known upper bound is $O(n^{8/9})$, due to Gowers [Go08].

```lean
theorem green_5.variants.gowers_sl_two :
    ∃ C > (0 : ℝ), ∀ (p : ℕ) [Fact p.Prime], ∀ S : Finset (SL₂ p),
      IsProductFree (S : Set (SL₂ p)) →
      (S.card : ℝ) ≤ C * (Fintype.card (SL₂ p) : ℝ) ^ ((8 : ℝ) / 9)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/GreensOpenProblems/5.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/5.lean#L94).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/5.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/5.lean)
- [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.5)
