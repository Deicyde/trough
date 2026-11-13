---
declaration: lemma
origin: cited
lean: DedekindNumber.exists_minimal_true_subset, DedekindNumber.fromSperner_toSperner, DedekindNumber.toSperner_fromSperner, DedekindNumber.M_eq_kisielewiczFormula, DedekindNumber.M_eq, DedekindNumber.Dedekind_10
statement: formalized
---

# Dedekind Numbers

> A Dedekind number `M(n)` counts the number of monotone Boolean functions on `n` variables,
> or equivalently, the number of antichains (Sperner families) in the Boolean lattice `2^[n]`.
>
> For example,
>
> $$M ( 0 ) = 2 , M ( 1 ) = 3 , M ( 2 ) = 6 , and M ( 3 ) = 20 .$$
>
> The first few values grew slowly:
>
> $$M ( 4 ) = 168 , M ( 5 ) = 7581$$
>
> ,
> but then rapidly:
>
> $$M ( 6 ) = 7828354 , M ( 7 ) = 2414682040998 , M ( 8 ) = 56130437228687557907788$$
>
> , and
>
> $$M ( 9 ) = 286386577668298411128469151667598498812366$$
>
> (computed in 2023).
>
> We formalize two definitions:
> - `M n`: the number of monotone Boolean functions `(Fin n → Bool) → Bool`
> - `M' n`: the number of antichains (Sperner families) of `Finset (Fin n)`
>
> We prove their values for small `n` and show that the two definitions agree for all `n`.
>
> The problem is to determine the exact values of $M(n)$ for $n ≥ 10$.
> In particular, the value of $M(10)$ is currently unknown.
>
> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Dedekind_number)
> - [Oeis/A372](https://oeis.org/A000372)

*Quoted from [FormalConjectures/Wikipedia/DedekindNumber.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/DedekindNumber.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 6 research or textbook statements: 2 open, 1 solved and 3 textbook results. It also has 13 test statements and 6 API statements, counted here but not shown.

## `DedekindNumber.exists_minimal_true_subset`

Textbook result, proved here.

> Every true set of a monotone Boolean function contains a minimal true set.

```lean
lemma exists_minimal_true_subset {n : ℕ} {f : (Fin n → Bool) → Bool} (_ : Monotone f)
    {s : Finset (Fin n)} (hs : f (χ s) = true) :
    ∃ t, t ⊆ s ∧ f (χ t) = true ∧ ∀ u, u ⊆ t → f (χ u) = true → t ⊆ u
```

Category `textbook`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [06 Order, lattices, ordered algebraic structures](../../by-subject/part-01/06-order-lattices-ordered-algebraic-structures/README.md). Declared in [FormalConjectures/Wikipedia/DedekindNumber.lean, line 168](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/DedekindNumber.lean#L168).

## `DedekindNumber.fromSperner_toSperner`

Textbook result, proved here.

> Converting a monotone function to a Sperner family and back yields the same function.

```lean
lemma fromSperner_toSperner {n : ℕ} (f : (Fin n → Bool) → Bool) (hf : Monotone f) :
    fromSperner (toSperner f) = f
```

Category `textbook`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [06 Order, lattices, ordered algebraic structures](../../by-subject/part-01/06-order-lattices-ordered-algebraic-structures/README.md). Declared in [FormalConjectures/Wikipedia/DedekindNumber.lean, line 184](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/DedekindNumber.lean#L184).

## `DedekindNumber.toSperner_fromSperner`

Textbook result, proved here.

> Converting a Sperner family to a monotone function and back yields the same family.

```lean
lemma toSperner_fromSperner {n : ℕ} (A : Finset (Finset (Fin n))) (hA : IsSperner A) :
    toSperner (fromSperner A) = A
```

Category `textbook`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [06 Order, lattices, ordered algebraic structures](../../by-subject/part-01/06-order-lattices-ordered-algebraic-structures/README.md). Declared in [FormalConjectures/Wikipedia/DedekindNumber.lean, line 203](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/DedekindNumber.lean#L203).

## `DedekindNumber.M_eq_kisielewiczFormula`

Solved: stated here without proof.

> Kisielewicz (1988) proved the following arithmetic formula for the Dedekind numbers:
>
> $$
>   M(n) = \sum_{k=0}^{2^{2^n}}\prod_{j = 1}^{2 ^ n - 1}\prod_{i = 0}^{j - 1} \left(
>     1 - b_i^kb_j^k \prod_{m = 0}^{\log_2 i} (1 - b_m^i + b_m^ib_m^j)\right),
> $$
>
> where $b_i^k$ is the $i$-th bit of $k$. However, this formula is not computationally
> efficient for large $n$.

```lean
theorem M_eq_kisielewiczFormula : M = kisielewiczFormula
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [06 Order, lattices, ordered algebraic structures](../../by-subject/part-01/06-order-lattices-ordered-algebraic-structures/README.md). Declared in [FormalConjectures/Wikipedia/DedekindNumber.lean, line 259](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/DedekindNumber.lean#L259).

## `DedekindNumber.M_eq`

Open: stated without proof.

> No closed-form expression that allows efficient computation of Dedekind numbers is
> currently known.

```lean
theorem M_eq : M = M_eq.answer
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [06 Order, lattices, ordered algebraic structures](../../by-subject/part-01/06-order-lattices-ordered-algebraic-structures/README.md). Declared in [FormalConjectures/Wikipedia/DedekindNumber.lean, line 269](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/DedekindNumber.lean#L269).

## `DedekindNumber.Dedekind_10`

Open: stated without proof.

> In particular, the Dedekind number for `n = 10` is currently unknown.

```lean
theorem Dedekind_10 : M 10 = Dedekind_10.answer
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [06 Order, lattices, ordered algebraic structures](../../by-subject/part-01/06-order-lattices-ordered-algebraic-structures/README.md). Declared in [FormalConjectures/Wikipedia/DedekindNumber.lean, line 278](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/DedekindNumber.lean#L278).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/DedekindNumber.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/DedekindNumber.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Dedekind_number)
