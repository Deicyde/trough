---
declaration: section
origin: cited
lean: Algebra.forall_isRegularRing_tensorProduct_essFiniteType_iff_finite_isPurelyInseparable, Algebra.IsGeometricallyRegular, Algebra.IsGeometricallyRegular.of_faithfullyFlat, Algebra.IsGeometricallyRegular.of_smooth, Algebra.IsGeometricallyRegular.of_directed_of_iSup_eq_top, Algebra.isGeometricallyRegular_iff_tower_top_of_isSeparable
statement: formalized
proof: formalized
---

# 10.166 Geometrically regular algebras

Section 10.166 of the Stacks Project, [Tag 045K](https://stacks.math.columbia.edu/tag/045K). 6 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0381, a lemma

[Tag 0381](https://stacks.math.columbia.edu/tag/0381) in the Stacks Project.

**`Algebra.forall_isRegularRing_tensorProduct_essFiniteType_iff_finite_isPurelyInseparable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyRegular/FieldExtension.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GeometricallyRegular/FieldExtension.lean#L160). The attribute's comment: “Regular ring is Definition 00OD, that is Mathlib's `IsRegularRing`, which already contains Noetherianness; a finitely generated field extension is `Algebra.EssFiniteType` (`IntermediateField.fg_top_iff`) and a finite purely inseparable one is `Module.Finite` together with `IsPurelyInseparable`. The source's hypothesis that `A` be Noetherian is not assumed: it is implied by either side, since `A ≃ₐ[k] k ⊗[k] A`. The extension fields range over a single free universe, `w := u` giving the source's statement in full. See the module docstring.”. References: EGA 0 (22.5.8), “b) ⇔ b')”; EGA IV (6.7.7), “(b) ⇔ (c), special case”.

> **Regularity of all base changes to finitely generated field extensions is detected by the
> finite purely inseparable ones.** Let `k` be a field and `A` a `k`-algebra. Then `K ⊗[k] A` is a
> regular ring (Definition 00OD) for every finitely generated field extension `K/k` if and only if
> `k' ⊗[k] A` is a regular ring for every finite purely inseparable extension `k'/k`.

```lean
public theorem forall_isRegularRing_tensorProduct_essFiniteType_iff_finite_isPurelyInseparable
    (k : Type u) (A : Type v) [Field k] [CommRing A] [Algebra k A] :
    (∀ (K : Type w) [Field K] [Algebra k K] [Algebra.EssFiniteType k K],
        IsRegularRing (K ⊗[k] A)) ↔
      ∀ (K : Type w) [Field K] [Algebra k K] [Module.Finite k K] [IsPurelyInseparable k K],
        IsRegularRing (K ⊗[k] A)
```

## Tag 0382, a definition

[Tag 0382](https://stacks.math.columbia.edu/tag/0382) in the Stacks Project.

**`Algebra.IsGeometricallyRegular`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyRegular/Defs.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GeometricallyRegular/Defs.lean#L140). The attribute's comment: “Stated as condition (1) of Lemma 0381; condition (2) follows by instance resolution and the converse is that lemma. Regular ring is Definition 00OD, that is Mathlib's `IsRegularRing`, which already contains Noetherianness, so the source's hypothesis that `R` be Noetherian is not assumed but implied (take `K := k`). A finitely generated field extension is `Algebra.EssFiniteType` (`IntermediateField.essFiniteType_iff`), and the test field ranges over the universe of `k`, which is the source's condition for extensions in every universe. See the module docstring.”. References: EGA IV (6.7.6).

> A `k`-algebra `R` over a field `k` is *geometrically regular over `k`* if `K ⊗[k] R` is a
> regular ring (Definition 00OD) for every finitely generated field extension `K/k`. By Lemma 0381
> it is enough to require this for the finite purely inseparable extensions `k'/k`.

```lean
public class IsGeometricallyRegular (k : Type u) (R : Type v) [Field k] [CommRing R]
    [Algebra k R] : Prop
```

## Tag 07NH, a lemma

[Tag 07NH](https://stacks.math.columbia.edu/tag/07NH) in the Stacks Project.

**`Algebra.IsGeometricallyRegular.of_faithfullyFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyRegular/FaithfullyFlatDescent.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GeometricallyRegular/FaithfullyFlatDescent.lean#L79). The attribute's comment: “The source's faithfully flat `k`-algebra map `A → B` is `Algebra A B` with `IsScalarTower k A B` and `Module.FaithfullyFlat A B`, the latter being `(algebraMap A B).FaithfullyFlat` by `RingHom.faithfullyFlat_algebraMap_iff`; geometric regularity is `Algebra.IsGeometricallyRegular` (Definition 0382), which already implies the Noetherianness the source assumes. Named after the sibling 07NG, `IsRegularRing.of_faithfullyFlat`. See the module docstring.”.

> **Geometric regularity descends through faithfully flat maps of algebras.**
> Let `k` be a field and let `A → B` be a faithfully flat map of `k`-algebras. If `B` is
> geometrically regular over `k`, then so is `A`.

```lean
public theorem IsGeometricallyRegular.of_faithfullyFlat {k : Type u} {A : Type v} (B : Type w)
    [Field k] [CommRing A] [CommRing B] [Algebra k A] [Algebra k B] [Algebra A B]
    [IsScalarTower k A B] [Module.FaithfullyFlat A B] [IsGeometricallyRegular k B] :
    IsGeometricallyRegular k A
```

## Tag 07QF, a lemma

[Tag 07QF](https://stacks.math.columbia.edu/tag/07QF) in the Stacks Project.

**`Algebra.IsGeometricallyRegular.of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyRegular/Smooth.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GeometricallyRegular/Smooth.lean#L89). The attribute's comment: “The source's smooth `k`-algebra map `A → B` is `Algebra A B` with `IsScalarTower k A B` and `Algebra.Smooth A B`, the latter being `(algebraMap A B).Smooth` by `RingHom.smooth_algebraMap` and being Definition 00T2 by Proposition 00TN; geometric regularity is `Algebra.IsGeometricallyRegular` (Definition 0382), which already implies the Noetherianness Definition 0382 assumes. Named after the sibling 07NH, `IsGeometricallyRegular.of_faithfullyFlat`. See the module docstring.”.

> **Geometric regularity ascends along smooth maps of algebras.** Let `k` be a field and let
> `A → B` be a smooth map of `k`-algebras. If `A` is geometrically regular over `k`, then so is
> `B`.

```lean
public theorem IsGeometricallyRegular.of_smooth {k : Type u} (A : Type v) {B : Type w}
    [Field k] [CommRing A] [CommRing B] [Algebra k A] [Algebra k B] [Algebra A B]
    [IsScalarTower k A B] [Algebra.Smooth A B] [IsGeometricallyRegular k A] :
    IsGeometricallyRegular k B
```

## Tag 07QG, a lemma

[Tag 07QG](https://stacks.math.columbia.edu/tag/07QG) in the Stacks Project.

**`Algebra.IsGeometricallyRegular.of_directed_of_iSup_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyRegular/Colimit.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GeometricallyRegular/Colimit.lean#L171). The attribute's comment: “The source's `k = colim k_i` over subfields is a directed family `t : ι → Subfield k` with `⨆ i, t i = ⊤`, equivalently (`Subfield.mem_iSup_of_directed`) every element of `k` lying in some `t i`; `Nonempty ι` is necessary, since for `ι` empty and `k` a prime field the supremum is `⊤` and the hypothesis vacuous. `A` is a `t i`-algebra by restriction of scalars along `t i ↪ k` (`IsScalarTower ↥(t i) k A`), and geometric regularity is `Algebra.IsGeometricallyRegular` (Definition 0382), which already implies the Noetherianness Definition 0382 assumes. See the module docstring.”.

> Let `k` be a field, `A` a `k`-algebra, and let `t : ι → Subfield k` be a nonempty directed
> family of subfields of `k` with `⨆ i, t i = ⊤`, that is, `k = colim (t i)`. If `A` is
> geometrically regular over every `t i`, then `A` is geometrically regular over `k`.

```lean
public theorem IsGeometricallyRegular.of_directed_of_iSup_eq_top {k : Type u} {A : Type v}
    {ι : Type w} [Nonempty ι] [Field k] [CommRing A] [Algebra k A] (t : ι → Subfield k)
    (dir : Directed (· ≤ ·) t) (htop : ⨆ i, t i = ⊤)
    [∀ i, IsGeometricallyRegular (t i) A] :
    IsGeometricallyRegular k A
```

## Tag 07QH, a lemma

[Tag 07QH](https://stacks.math.columbia.edu/tag/07QH) in the Stacks Project.

**`Algebra.isGeometricallyRegular_iff_tower_top_of_isSeparable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyRegular/BaseFieldExtension.lean, line 219](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GeometricallyRegular/BaseFieldExtension.lean#L219). The attribute's comment: “The source's separable algebraic extension `k'/k` is `Algebra.IsSeparable k k'`, which already contains algebraicity (`Algebra.IsSeparable.isAlgebraic`); no finiteness is assumed, the reduction to the finite case being internal to the proof (Lemma 07QG). `A` being an algebra over `k'` and over `k` at once is `IsScalarTower k k' A`, which pins the `k`-structure to be the restriction of the `k'`-structure. Geometric regularity is `Algebra.IsGeometricallyRegular` (Definition 0382), which already implies the Noetherianness Definition 0382 assumes. Named after Mathlib's `Algebra.isSeparable_tower_top_of_isSeparable`, `tower_top` naming the right-hand side. See the module docstring.”.

> Let `k'/k` be a separable algebraic field extension and let `A` be a `k'`-algebra, viewed as a
> `k`-algebra by restriction of scalars. Then `A` is geometrically regular over `k` if and only if
> it is geometrically regular over `k'`.

```lean
public theorem isGeometricallyRegular_iff_tower_top_of_isSeparable (k : Type u) (k' : Type v)
    (A : Type w) [Field k] [Field k'] [CommRing A] [Algebra k k'] [Algebra k A] [Algebra k' A]
    [IsScalarTower k k' A] [Algebra.IsSeparable k k'] :
    IsGeometricallyRegular k A ↔ IsGeometricallyRegular k' A
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.166, Tag 045K](https://stacks.math.columbia.edu/tag/045K)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
