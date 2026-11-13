---
declaration: theorem
origin: cited
lean: Arxiv.«math.0703548».projective_module_isStablyFree, Arxiv.«math.0703548».bass_conjecture_integral_domain
statement: formalized
---

# Algebraic consequences of the Farrell–Jones conjecture

> The assembly map in the Farrell–Jones conjecture is not yet available in Mathlib. This file
> states two of its algebraic consequences using projective modules and matrices over group rings:
> the vanishing of the reduced projective class group and the Bass conjecture for commutative
> integral domains.
>
> *Reference:*
> - [BLR08] [arxiv/math.0703548](https://arxiv.org/abs/math/0703548)
>   **On the Farrell–Jones Conjecture and its applications**
>   by *Arthur Bartels, Wolfgang Lück, Holger Reich*, J. Topol. 1 (2008), 57–86.

*Quoted from [FormalConjectures/Arxiv/math.0703548/FarrellJonesConsequences.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/math.0703548/FarrellJonesConsequences.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 2 API statements, counted here but not shown.

## `Arxiv.«math.0703548».projective_module_isStablyFree`

Open: stated without proof.

> **Vanishing of the reduced projective class group for integral group rings.**
>
> If `G` is torsion-free, that is, if its only element of finite order is `1`, then every finitely
> generated projective module over `ℤ[G]` is stably free. This is the stable-freeness form of the
> vanishing of $\widetilde K_0(\mathbb{Z}[G])$, which is the conclusion of Theorem 0.2 (ii) of
> [BLR08] for the regular ring $\mathbb{Z}$. That theorem assumes the K-theoretic Farrell–Jones
> conjecture for `G` with coefficients in `ℤ`.

```lean
theorem projective_module_isStablyFree {G : Type*} [Group G] (hG : ∀ g : G, IsOfFinOrder g → g = 1)
    (M : Type*) [AddCommGroup M] [Module (MonoidAlgebra ℤ G) M]
    [Module.Finite (MonoidAlgebra ℤ G) M] [Module.Projective (MonoidAlgebra ℤ G) M] :
    Module.IsStablyFree (MonoidAlgebra ℤ G) M
```

Category `research open`; AMS [16 Associative rings and algebras](../../by-subject/part-01/16-associative-rings-and-algebras/README.md), [19 K-theory](../../by-subject/part-01/19-k-theory/README.md), [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/Arxiv/math.0703548/FarrellJonesConsequences.lean, line 82](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/math.0703548/FarrellJonesConsequences.lean#L82).

## `Arxiv.«math.0703548».bass_conjecture_integral_domain`

Open: stated without proof.

> **Bass conjecture for commutative integral domains, in idempotent-matrix form.**
>
> Let `A` be an idempotent matrix over `R[G]`. If the order of `g` is not invertible in `R`, then
> the Hattori–Stallings trace of the projective module represented by `A` vanishes at the conjugacy
> class of `g`. This includes every infinite-order `g`, whose `orderOf` is zero. This is
> Conjecture 0.6 of [BLR08]. By Theorems 0.5 (ii) and 0.7 of [BLR08] it follows from the
> Farrell–Jones conjecture with coefficients in every field of prime characteristic.

```lean
theorem bass_conjecture_integral_domain {R : Type*} [CommRing R] [IsDomain R] {G : Type*}
    [Group G] {n : Type*} [Fintype n] (A : Matrix n n (MonoidAlgebra R G))
    (hA : A * A = A) (g : G) (hg : ¬IsUnit (orderOf g : R)) :
    matrixHattoriStallingsTraceAt A g = 0
```

Category `research open`; AMS [16 Associative rings and algebras](../../by-subject/part-01/16-associative-rings-and-algebras/README.md), [19 K-theory](../../by-subject/part-01/19-k-theory/README.md), [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/Arxiv/math.0703548/FarrellJonesConsequences.lean, line 98](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/math.0703548/FarrellJonesConsequences.lean#L98).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Arxiv/math.0703548/FarrellJonesConsequences.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/math.0703548/FarrellJonesConsequences.lean)
- [arxiv/math.0703548](https://arxiv.org/abs/math/0703548)
