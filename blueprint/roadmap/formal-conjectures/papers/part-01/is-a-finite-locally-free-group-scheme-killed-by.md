---
declaration: theorem
origin: cited
lean: FiniteLocallyFreeGroupSchemeExponent.killed_by_rank, FiniteLocallyFreeGroupSchemeExponent.killed_by_rank.variants.field, FiniteLocallyFreeGroupSchemeExponent.killed_by_rank.variants.reduced_base, FiniteLocallyFreeGroupSchemeExponent.killed_by_rank.variants.commutative, FiniteLocallyFreeGroupSchemeExponent.optimal_exponent
statement: formalized
---

# Is a finite locally free group scheme killed by its order?

> A finite locally free group scheme of rank `n` is the group scheme analogue of a finite group of
> order `n`. Lagrange's theorem gives `g ^ n = 1` in a finite group of order `n`, and Grothendieck
> asked whether the `n`-th power map of such a group scheme is trivial. The answer is affirmative
> over a reduced base and for commutative group schemes, and negative in general. Which exponents
> kill every group scheme of a given rank is open.
>
> A group scheme is represented here by its coordinate Hopf algebra `A` over the base ring `R`.
> `A` is not assumed to be cocommutative, so the group scheme is not assumed to be commutative.
> The base is a ring rather than a scheme: a finite locally free group scheme is affine over its
> base, and being killed by `m` is local on the base, so nothing is lost.
>
> *References:*
> - [M. Demazure and A. Grothendieck, *Schémas en groupes* (SGA 3), re-edition by P. Gille and
>   P. Polo](https://webusers.imj-prg.fr/~patrick.polo/SGA3/). Exp. VIII, Rem. 7.3.1 poses the
>   question; an editors' note records that the re-edition drops the commutativity assumption there.
>   Exp. VIIA, Prop. 8.5 settles the case of a field and Cor. 8.5.2 the case of a reduced base.
> - [R. Schoof, *Is a finite locally free group scheme killed by its
>   order?*](https://reneschoof.github.io/schoof_oortAAG.pdf), a survey of the question and of the
>   cases that are known, written before the counterexample
> - [J. Tate and F. Oort, *Group schemes of prime order*](https://www.numdam.org/item/ASENS_1970_4_3_1_1_0/),
>   p. 4 for Deligne's theorem and p. 5, which records the general question as open in 1970
> - [Mathlib, *A finite free group scheme of rank four that is not killed by
>   four*](https://leanprover-community.github.io/mathlib4_docs/Counterexamples/GrothendieckPower.html),
>   the counterexample

*Quoted from [FormalConjectures/Paper/FiniteLocallyFreeGroupSchemeExponent.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/FiniteLocallyFreeGroupSchemeExponent.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 5 research or textbook statements: 1 open and 4 solved. It also has 5 test statements and 2 API statements, counted here but not shown.

## `FiniteLocallyFreeGroupSchemeExponent.killed_by_rank`

Solved: stated here; a Lean proof is at [https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Counterexamples/GrothendieckPower.lean#L882-L892](https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Counterexamples/GrothendieckPower.lean#L882-L892).

> Grothendieck's question: is every finite locally free group scheme of rank $n$, over every
> commutative ring, killed by $n$?
>
> The answer is no. There is a commutative Hopf algebra of rank $4$ over a finite non-reduced ring
> whose fourth power map is not trivial; its eighth power map is trivial. The formalised
> counterexample lives in `Type`, so the statement quantifies over rings and algebras in `Type`.

```lean
theorem killed_by_rank :
    ¬ ∀ n : ℕ+, IsUniversalKillingExponent.{0, 0} n n
```

Category `research solved`; AMS [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [16 Associative rings and algebras](../../by-subject/part-01/16-associative-rings-and-algebras/README.md). Declared in [FormalConjectures/Paper/FiniteLocallyFreeGroupSchemeExponent.lean, line 157](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/FiniteLocallyFreeGroupSchemeExponent.lean#L157).

## `FiniteLocallyFreeGroupSchemeExponent.killed_by_rank.variants.field`

Solved: stated here without proof.

> Over a field the answer is affirmative: a finite group scheme of rank $n$ over a field is killed
> by $n$. This is [SGA 3], Exp. VIIA, Prop. 8.5.

```lean
theorem killed_by_rank.variants.field (n : ℕ+) (k : Type*) [Field k] (A : Type*) [CommRing A]
    [HopfAlgebra k A] [Module.Finite k A] (hn : Module.finrank k A = (n : ℕ)) :
    IsKilledBy k A n
```

Category `research solved`; AMS [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [16 Associative rings and algebras](../../by-subject/part-01/16-associative-rings-and-algebras/README.md). Declared in [FormalConjectures/Paper/FiniteLocallyFreeGroupSchemeExponent.lean, line 166](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/FiniteLocallyFreeGroupSchemeExponent.lean#L166).

## `FiniteLocallyFreeGroupSchemeExponent.killed_by_rank.variants.reduced_base`

Solved: stated here without proof.

> Over a reduced base ring the answer is affirmative: every finite locally free group scheme of
> rank $n$ over a reduced commutative ring is killed by $n$. This is [SGA 3], Exp. VIIA, Cor. 8.5.2,
> deduced there from the case of a field.

```lean
theorem killed_by_rank.variants.reduced_base (n : ℕ+) (R : Type*) [CommRing R] [IsReduced R]
    (A : Type*) [CommRing A] [HopfAlgebra R A] [Module.Finite R A] [Module.Projective R A]
    (hn : Module.rankAtStalk (R := R) A = fun _ ↦ (n : ℕ)) :
    IsKilledBy R A n
```

Category `research solved`; AMS [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [16 Associative rings and algebras](../../by-subject/part-01/16-associative-rings-and-algebras/README.md). Declared in [FormalConjectures/Paper/FiniteLocallyFreeGroupSchemeExponent.lean, line 177](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/FiniteLocallyFreeGroupSchemeExponent.lean#L177).

## `FiniteLocallyFreeGroupSchemeExponent.killed_by_rank.variants.commutative`

Solved: stated here without proof.

> Deligne's theorem: a finite locally free *commutative* group scheme of rank $n$ over any
> commutative ring is killed by $n$. Commutativity of the group scheme is cocommutativity of its
> coordinate Hopf algebra. See [SGA 3], Exp. VIIA, Rem. 8.5.3 and [TO70], p. 4.

```lean
theorem killed_by_rank.variants.commutative (n : ℕ+) (R : Type*) [CommRing R] (A : Type*)
    [CommRing A] [HopfAlgebra R A] [Coalgebra.IsCocomm R A] [Module.Finite R A]
    [Module.Projective R A]
    (hn : Module.rankAtStalk (R := R) A = fun _ ↦ (n : ℕ)) :
    IsKilledBy R A n
```

Category `research solved`; AMS [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [16 Associative rings and algebras](../../by-subject/part-01/16-associative-rings-and-algebras/README.md). Declared in [FormalConjectures/Paper/FiniteLocallyFreeGroupSchemeExponent.lean, line 189](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/FiniteLocallyFreeGroupSchemeExponent.lean#L189).

## `FiniteLocallyFreeGroupSchemeExponent.optimal_exponent`

Open: stated without proof.

> Determine the function assigning to each positive integer $n$ the least positive integer $m$
> such that every finite locally free group scheme of rank $n$, over every commutative ring, is
> killed by $m$. The value is $0$ if there is no such $m$, since `sInf ∅ = 0` in `ℕ`. As in
> `killed_by_rank`, the rings and algebras are in `Type`.
>
> Grothendieck asked whether this least exponent is $n$ itself. It is not, already for $n = 4$.
> If some positive exponent kills every group scheme of rank $n$, then these exponents are the
> multiples of the least one, so minimality for $\le$ agrees with minimality for divisibility.

```lean
theorem optimal_exponent :
    ∀ n, sInf ((↑) '' {m | IsUniversalKillingExponent.{0, 0} n m} : Set ℕ) = optimal_exponent.answer
      n
```

Category `research open`; AMS [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [16 Associative rings and algebras](../../by-subject/part-01/16-associative-rings-and-algebras/README.md). Declared in [FormalConjectures/Paper/FiniteLocallyFreeGroupSchemeExponent.lean, line 209](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/FiniteLocallyFreeGroupSchemeExponent.lean#L209).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/FiniteLocallyFreeGroupSchemeExponent.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/FiniteLocallyFreeGroupSchemeExponent.lean)
- [M. Demazure and A. Grothendieck, *Schémas en groupes* (SGA 3), re-edition by P. Gille and
  P. Polo](https://webusers.imj-prg.fr/~patrick.polo/SGA3/)
