---
declaration: section
origin: cited
lean: AlgebraicGeometry.ProEtale.IsIndZariski, Algebra.IsIndZariski.tensorProduct, Algebra.IsIndZariski.comp, AlgebraicGeometry.ProEtale.isIndZariski_of_left_of_comp, AlgebraicGeometry.ProEtale.isIndZariski_of_colimitPresentation, AlgebraicGeometry.ProEtale.identifiesLocalRings_of_isIndZariski, Algebra.IdentifiesLocalRings.of_isIndZariski
statement: formalized
proof: formalized
---

# 61.4 Ind-Zariski algebra

Section 61.4 of the Stacks Project, [Tag 096M](https://stacks.math.columbia.edu/tag/096M). 6 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 096N, a definition

[Tag 096N](https://stacks.math.columbia.edu/tag/096N) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.IsIndZariski`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/IndZariski/Basic.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/IndZariski/Basic.lean#L53).

> A commutative `A`-algebra is ind-Zariski if it is a filtered colimit of
> `A`-algebras whose structure maps are local isomorphisms. The stages and the lifted
> target lie in the maximum of the source and target carrier universes.

```lean
abbrev IsIndZariski (A : Type u) (B : Type v) [CommRing A] [CommRing B] [Algebra A B] : Prop
```

## Tag 096P, a lemma

[Tag 096P](https://stacks.math.columbia.edu/tag/096P) in the Stacks Project.

**`Algebra.IsIndZariski.tensorProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/IndZariski/BaseChange.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/IndZariski/BaseChange.lean#L72).

> The base change of an ind-Zariski algebra map is ind-Zariski: if `B` is ind-Zariski over `A`
> and `A'` is any `A`-algebra, then `B ⊗[A] A'` is ind-Zariski over `A'`.

```lean
theorem IsIndZariski.tensorProduct (A : Type u) (B : Type v) (A' : Type w) [CommRing A]
    [CommRing B] [CommRing A'] [Algebra A B] [Algebra A A'] (h : IsIndZariski A B) :
    IsIndZariski A' (B ⊗[A] A')
```

## Tag 096Q, a lemma

[Tag 096Q](https://stacks.math.columbia.edu/tag/096Q) in the Stacks Project.

**`Algebra.IsIndZariski.comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/IndZariski.lean, line 990](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/IndZariski.lean#L990).

> **Stacks 096Q.** If `B` is ind-Zariski over `A` and `C` is ind-Zariski over `B`, then `C` is
> ind-Zariski over `A`.

```lean
theorem Algebra.IsIndZariski.comp (A : Type u) (B : Type v) (C : Type w)
    [CommRing A] [CommRing B] [CommRing C]
    [Algebra A B] [Algebra B C] [Algebra A C] [IsScalarTower A B C]
    (hAB : Algebra.IsIndZariski A B) (hBC : Algebra.IsIndZariski B C) :
    Algebra.IsIndZariski A C
```

## Tag 096R, a lemma

[Tag 096R](https://stacks.math.columbia.edu/tag/096R) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.isIndZariski_of_left_of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/IndZariski/Permanence.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/IndZariski/Permanence.lean#L150).

> **Stacks 096R.** Ind-Zariski maps cancel on the left in an algebra tower: if `B` and `C` are
> ind-Zariski over `A`, then `C` is ind-Zariski over `B`.

```lean
theorem isIndZariski_of_left_of_comp (A : Type u) (B : Type v) (C : Type w)
    [CommRing A] [CommRing B] [CommRing C]
    [Algebra A B] [Algebra B C] [Algebra A C] [IsScalarTower A B C]
    (hAB : Algebra.IsIndZariski A B) (hAC : Algebra.IsIndZariski A C) :
    Algebra.IsIndZariski B C
```

## Tag 096S, a lemma

[Tag 096S](https://stacks.math.columbia.edu/tag/096S) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.isIndZariski_of_colimitPresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/IndZariski/FilteredColimit.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/IndZariski/FilteredColimit.lean#L96).

> **Stacks 096S.** A filtered colimit of ind-Zariski `A`-algebras is ind-Zariski over `A`: if
> `B` is presented as the colimit of a filtered diagram of `A`-algebras each of which is ind-Zariski
> over `A`, then `B` is ind-Zariski over `A`.

```lean
theorem isIndZariski_of_colimitPresentation {A : Type u} {B : Type v} [CommRing A] [CommRing B]
    [Algebra A B] {J : Type*} [Category* J] [IsFiltered J] [EssentiallySmall.{max u v} J]
    (pres : ColimitPresentation J (CommAlgCat.of A (ULift.{u} B)))
    (hpres : ∀ j, Algebra.IsIndZariski A (pres.diag.obj j)) :
    Algebra.IsIndZariski A B
```

## Tag 096T, a lemma

[Tag 096T](https://stacks.math.columbia.edu/tag/096T) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.identifiesLocalRings_of_isIndZariski`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/IndZariski/LocalRings.lean, line 329](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/IndZariski/LocalRings.lean#L329).

> An ind-Zariski map identifies the local rings at every prime of its target.

```lean
theorem identifiesLocalRings_of_isIndZariski
    (A : Type u) (B : Type v) [CommRing A] [CommRing B] [Algebra A B]
    (h : IsIndZariski.{u, v, w} A B) :
    Algebra.IdentifiesLocalRings A B
```

**`Algebra.IdentifiesLocalRings.of_isIndZariski`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/IndZariski/IdentifiesLocalRings.lean, line 347](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/IndZariski/IdentifiesLocalRings.lean#L347).

> **Stacks 096T.** An ind-Zariski algebra identifies local rings: for every prime `q` of `B`
> the canonical map from the localization of `A` at the preimage of `q` to the localization of
> `B` at `q` is bijective.

```lean
theorem Algebra.IdentifiesLocalRings.of_isIndZariski {A : Type u} {B : Type v} [CommRing A]
    [CommRing B] [Algebra A B] (h : Algebra.IsIndZariski A B) :
    Algebra.IdentifiesLocalRings A B
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 61.4, Tag 096M](https://stacks.math.columbia.edu/tag/096M)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
