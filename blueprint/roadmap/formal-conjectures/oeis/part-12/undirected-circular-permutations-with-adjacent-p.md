---
declaration: theorem
origin: cited
lean: OeisA229232.conjecture_1, OeisA229232.conjecture_2, OeisA229232.conjecture_3, OeisA229232.conjecture_4, OeisA229232.conjecture_5
statement: formalized
---

# Undirected circular permutations with adjacent products minus one all prime

> Number of undirected circular permutations $\pi(1), \dots, \pi(n)$ of $1, \dots, n$ with the $n$
> numbers $\pi(1)\pi(2)-1, \pi(2)\pi(3)-1, \dots, \pi(n-1)\pi(n)-1, \pi(n)\pi(1)-1$ all prime.
>
> *References:*
> - [A229232](https://oeis.org/A229232)

*Quoted from [FormalConjectures/OEIS/229232.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/229232.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 5 research or textbook statements: 5 open. It also has 6 test statements, counted here but not shown.

## `OeisA229232.conjecture_1`

Open: stated without proof.

> Conjecture: $a(n) > 0$ for all $n > 5$ with $n$ not equal to $13$.

```lean
theorem conjecture_1 (n : ℕ) (hn : n > 5) (hne : n ≠ 13) : a n > 0
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/229232.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/229232.lean#L67).

## `OeisA229232.conjecture_2`

Open: stated without proof.

> Conjecture: For any integer $n > 1$, there is a permutation $\pi(1), \dots, \pi(n)$ of $1, \dots, n$
> such that the $n$ numbers $2\pi(1)\pi(2)-1, \dots, 2\pi(n-1)\pi(n)-1, 2\pi(n)\pi(1)-1$ are
> all prime.
> - _Zhi-Wei Sun_

```lean
theorem conjecture_2 (n : ℕ) (hn : n > 1) :
    ∃ π : Equiv.Perm (Fin n), ∀ i : Fin n,
      (2 * ((π i).val + 1) *
        ((π ⟨(i.val + 1) % n, Nat.mod_lt _ (by omega)⟩).val + 1) - 1).Prime
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/229232.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/229232.lean#L77).

## `OeisA229232.conjecture_3`

Open: stated without proof.

> Conjecture: For any positive integer $n$ not equal to $4$, there is a permutation
> $\pi(1), \dots, \pi(n)$ of $1, \dots, n$ such that the $n$ numbers
> $2\pi(1)\pi(2)+1, \dots, 2\pi(n-1)\pi(n)+1, 2\pi(n)\pi(1)+1$ are all prime.
> - _Zhi-Wei Sun_

```lean
theorem conjecture_3 (n : ℕ) (hn : n > 0) (hne : n ≠ 4) :
    ∃ π : Equiv.Perm (Fin n), ∀ i : Fin n,
      (2 * ((π i).val + 1) * ((π ⟨(i.val + 1) % n, Nat.mod_lt _ hn⟩).val + 1) + 1).Prime
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/229232.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/229232.lean#L90).

## `OeisA229232.conjecture_4`

Open: stated without proof.

> Conjecture: Let $F$ be a finite field with $q > 7$ elements. Then, there is a circular
> permutation $a_1, \dots, a_{q-1}$ of the $q-1$ nonzero elements of $F$ such that all the $q-1$
> elements $a_1 a_2 - 1, a_2 a_3 - 1, \dots, a_{q-2} a_{q-1} - 1, a_{q-1} a_1 - 1$ are
> primitive elements of the field $F$ (i.e., generators of the multiplicative group
> $F \setminus \{0\}$).
> - _Zhi-Wei Sun_

```lean
theorem conjecture_4 (F : Type*) [Field F] [Fintype F] (hF : Fintype.card F > 7) :
    let m := Fintype.card F - 1
    ∃ a : Fin m ≃ Fˣ,
      ∀ i : Fin m, IsPrimitiveRoot
        ((a i : F) * (a ⟨(i.val + 1) % m, Nat.mod_lt _ (by omega)⟩ : F) - 1) m
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/OEIS/229232.lean, line 104](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/229232.lean#L104).

## `OeisA229232.conjecture_5`

Open: stated without proof.

> Conjecture: Let $F$ be a finite field with $q > 7$ elements. There is a circular permutation
> $b_1, \dots, b_{q-1}$ of the $q-1$ nonzero elements of $F$ such that all the $q-1$ elements
> $b_1 b_2 + 1, b_2 b_3 + 1, \dots, b_{q-2} b_{q-1} + 1, b_{q-1} b_1 + 1$ are primitive elements
> of the field $F$ (i.e., generators of the multiplicative group $F \setminus \{0\}$).
> - _Zhi-Wei Sun_

```lean
theorem conjecture_5 (F : Type*) [Field F] [Fintype F] (hF : Fintype.card F > 7) :
    let m := Fintype.card F - 1
    ∃ b : Fin m ≃ Fˣ,
      ∀ i : Fin m, IsPrimitiveRoot
        ((b i : F) * (b ⟨(i.val + 1) % m, Nat.mod_lt _ (by omega)⟩ : F) + 1) m
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/OEIS/229232.lean, line 119](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/229232.lean#L119).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/229232.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/229232.lean)
- [A229232](https://oeis.org/A229232)
