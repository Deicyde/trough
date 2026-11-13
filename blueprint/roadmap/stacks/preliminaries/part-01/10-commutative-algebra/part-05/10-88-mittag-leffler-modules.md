---
declaration: section
origin: cited
lean: CategoryTheory.Functor.IsMittagLefflerSystem, LinearMap.Dominates, LinearMap.dominates_iff_forall_finitePresentation, dominates_iff_pushoutInl_universallyInjective, LinearMap.forall_ker_rTensor_le_iff_exists_eq_comp, CategoryTheory.Functor.tfae_isMittagLefflerSystem, IsMittagLeffler, CategoryTheory.Functor.isMittagLefflerSystem_iff_isMittagLeffler_dual
statement: formalized
proof: formalized
---

# 10.88 Mittag-Leffler modules

Section 10.88 of the Stacks Project, [Tag 0599](https://stacks.math.columbia.edu/tag/0599). 12 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 059A, a definition

[Tag 059A](https://stacks.math.columbia.edu/tag/059A) in the Stacks Project.

**`CategoryTheory.Functor.IsMittagLefflerSystem`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/MittagLeffler/Defs.lean, line 128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/MittagLeffler/Defs.lean#L128).

> **Stacks 059A.** A diagram `F : J ⥤ ModuleCat R` of `R`-modules, thought of as a directed
> system `(M i, f i j)`, is a *Mittag-Leffler system* if every `M i` is an `R`-module of finite
> presentation and if for every `R`-module `N` the inverse system of dual modules
> `(Hom_R(M i, N), Hom_R(f i j, N))`, that is `F.op ⋙ yoneda.obj N`, satisfies the Mittag-Leffler
> condition.

```lean
public def IsMittagLefflerSystem {R : Type u} [Ring R] {J : Type w} [Category.{w'} J]
    (F : J ⥤ ModuleCat.{v} R) : Prop
```

## Tag 059B, a definition

[Tag 059B](https://stacks.math.columbia.edu/tag/059B) in the Stacks Project.

**`LinearMap.Dominates`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/Dominates.lean, line 136](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/Dominates.lean#L136). The attribute's comment: “Domination is spelled out as containment of the kernels of the two maps tensored with the identity of the test module.”.

> **Stacks 059B.** Let `f : M → N` and `g : M → M'` be maps of `R`-modules with common source.
> We say `g` *dominates* `f` if for every `R`-module `Q` we have
> `Ker(f ⊗_R id_Q) ⊆ Ker(g ⊗_R id_Q)` as submodules of `M ⊗_R Q`.

```lean
public def Dominates {R : Type u} [CommSemiring R] {M : Type v} {N : Type w} {M' : Type w'}
    [AddCommMonoid M] [Module R M] [AddCommMonoid N] [Module R N] [AddCommMonoid M']
    [Module R M'] (g : M →ₗ[R] M') (f : M →ₗ[R] N) : Prop
```

## Tag 059C, a lemma

[Tag 059C](https://stacks.math.columbia.edu/tag/059C) in the Stacks Project.

**`LinearMap.dominates_iff_forall_finitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/Dominates.lean, line 451](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/Dominates.lean#L451). The attribute's comment: “Domination is the project's `LinearMap.Dominates`; the containment of kernels is the containment of the kernels of the maps tensored with the identity of the test module.”.

> **Stacks 059C.** Let `f : M → N` and `g : M → M'` be maps of `R`-modules. Then `g` dominates
> `f`, that is `Ker(f ⊗_R id_Q) ⊆ Ker(g ⊗_R id_Q)` for every `R`-module `Q`, if and only if
> `Ker(f ⊗_R id_Q) ⊆ Ker(g ⊗_R id_Q)` for every finitely presented `R`-module `Q`.

```lean
public theorem LinearMap.dominates_iff_forall_finitePresentation {R : Type u} [CommRing R]
    [Small.{v} R] {M : Type v} {N : Type w} {M' : Type w'} [AddCommGroup M] [Module R M]
    [AddCommGroup N] [Module R N] [AddCommGroup M'] [Module R M'] (g : M →ₗ[R] M')
    (f : M →ₗ[R] N) :
    g.Dominates f ↔
      ∀ (Q : Type v) [AddCommGroup Q] [Module R Q] [Module.FinitePresentation R Q],
        LinearMap.ker (f.rTensor Q) ≤ LinearMap.ker (g.rTensor Q)
```

## Tag 0AUM, a lemma

[Tag 0AUM](https://stacks.math.columbia.edu/tag/0AUM) in the Stacks Project.

**`dominates_iff_pushoutInl_universallyInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/Dominates.lean, line 621](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/Dominates.lean#L621).

> Let `f : M → N` and `g : M → M'` be maps of `R`-modules, and form the pushout
> square `f' : M' → N'`, `g' : N → N'`. Then `g` dominates `f` if and only if `f'`
> is universally injective.

```lean
theorem dominates_iff_pushoutInl_universallyInjective
    {M N M' : Type u} [AddCommGroup M] [Module R M]
    [AddCommGroup N] [Module R N] [AddCommGroup M'] [Module R M']
    (f : M →ₗ[R] N) (g : M →ₗ[R] M') :
    Dominates.{u, u, u, u, u} f g ↔ UniversallyInjective (pushoutInl f g)
```

## Tag 059D, a lemma

[Tag 059D](https://stacks.math.columbia.edu/tag/059D) in the Stacks Project.

**`LinearMap.forall_ker_rTensor_le_iff_exists_eq_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/Factorization.lean, line 296](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/Factorization.lean#L296). The attribute's comment: “Domination is spelled out as containment of the kernels of the tensored maps.”.

> **Stacks 059D.** Let `f : M → N` and `g : M → M'` be maps of `R`-modules and suppose that
> `Coker(f) = N ⧸ Im(f)` is of finite presentation. Then `g` dominates `f`, that is
> `Ker(f ⊗ id_Q) ⊆ Ker(g ⊗ id_Q)` for every `R`-module `Q`, if and only if `g` factors through `f`,
> that is `g = h ∘ f` for some module map `h : N → M'`.

```lean
public theorem LinearMap.forall_ker_rTensor_le_iff_exists_eq_comp {R : Type u} [CommRing R]
    [Small.{v} R] {M N M' : Type v} [AddCommGroup M] [Module R M] [AddCommGroup N] [Module R N]
    [AddCommGroup M'] [Module R M'] (f : M →ₗ[R] N) (g : M →ₗ[R] M')
    [Module.FinitePresentation R (N ⧸ LinearMap.range f)] :
    (∀ (Q : Type v) [AddCommGroup Q] [Module R Q],
        LinearMap.ker (f.rTensor Q) ≤ LinearMap.ker (g.rTensor Q)) ↔
      ∃ h : N →ₗ[R] M', g = h ∘ₗ f
```

## Tag 059E, a proposition

[Tag 059E](https://stacks.math.columbia.edu/tag/059E) in the Stacks Project.

**`CategoryTheory.Functor.tfae_isMittagLefflerSystem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/MittagLeffler/Criteria.lean, line 519](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/MittagLeffler/Criteria.lean#L519). The attribute's comment: “Domination is spelled out as containment of the kernels of the tensored maps; condition (4) is 059A's `IsMittagLefflerSystem`.”.

> **Stacks 059E.** Let `R` be a commutative ring, let `F : J ⥤ ModuleCat R` be a directed system
> `(M i, f i j)` of finitely presented `R`-modules over a nonempty directed preorder `J`, and let `c`
> be a colimit cocone on `F`, so that `M = c.pt` is `colim_{i ∈ J} M i` with canonical maps
> `f i : M i → M`. The following are equivalent:
>
> 1. for every finitely presented `R`-module `P` and every map `f : P → M` there are a finitely
>    presented `R`-module `Q` and a map `g : P → Q` which dominate each other, that is
>    `Ker(f ⊗ id_T) = Ker(g ⊗ id_T)` for every `R`-module `T`;
> 2. for each `i` there is a `j ≥ i` such that `f i j` dominates `f i`, that is
>    `Ker(f i ⊗ id_T) ⊆ Ker(f i j ⊗ id_T)` for every `R`-module `T`;
> 3. for each `i` there is a `j ≥ i` such that `f i j` factors through `f i k` for every `k ≥ i`;
> 4. `F` is a Mittag-Leffler system: the inverse system `(Hom_R(M i, T), Hom_R(f i j, T))` is
>    Mittag-Leffler for every `R`-module `T`;
> 5. that inverse system is Mittag-Leffler for the single module `T = ∏_{s ∈ J} M s`.

```lean
public theorem tfae_isMittagLefflerSystem {R : Type u} [CommRing R] [Small.{w} R] {J : Type w}
    [Preorder J] [IsDirectedOrder J] [Nonempty J] (F : J ⥤ ModuleCat.{w} R)
    [∀ i, Module.FinitePresentation R (F.obj i)] {c : Cocone F} (hc : IsColimit c) :
    List.TFAE
      [∀ (P : ModuleCat.{w} R) [Module.FinitePresentation R P] (f : P ⟶ c.pt),
          ∃ (Q : ModuleCat.{w} R) (_ : Module.FinitePresentation R Q) (g : P ⟶ Q),
            ∀ T : ModuleCat.{w} R,
              LinearMap.ker (f.hom.rTensor T) = LinearMap.ker (g.hom.rTensor T),
        ∀ i : J, ∃ (j : J) (u : i ⟶ j), ∀ T : ModuleCat.{w} R,
          LinearMap.ker ((c.ι.app i).hom.rTensor T) ≤ LinearMap.ker ((F.map u).hom.rTensor T),
        ∀ i : J, ∃ (j : J) (u : i ⟶ j), ∀ (k : J) (v : i ⟶ k),
          ∃ h : F.obj k ⟶ F.obj j, F.map u = F.map v ≫ h,
        F.IsMittagLefflerSystem,
        (F.op ⋙ yoneda.obj (ModuleCat.of R (∀ s : J, F.obj s))).IsMittagLeffler]
```

## Tag 059F, a definition

[Tag 059F](https://stacks.math.columbia.edu/tag/059F) in the Stacks Project.

**`IsMittagLeffler`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/MittagLeffler/Defs.lean, line 218](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/MittagLeffler/Defs.lean#L218).

> (Stacks 10.88.7, tag 059F.) An `R`-module `M` is *Mittag-Leffler* if for
> every finitely presented `R`-module `P` and every `R`-linear map `f : P → M`,
> there exists a finitely presented `R`-module `Q` and an `R`-linear map
> `g : P → Q` such that `f` and `g` dominate each other.
>
> This is condition (1) of Stacks Proposition 10.88.6 (tag 059E), which is
> equivalent to the other four conditions in that proposition. We choose this
> condition because it is intrinsic to `M` and does not depend on any auxiliary
> choice of a directed system writing `M` as a colimit of finitely presented
> modules.
>
> The universe parameters `uP`, `uQ`, `uN` are independent of `uR`, `uM`, so
> "for every finitely presented `R`-module `P`", "there exists ... `Q`", and
> "for every test module `N`" each range over their own arbitrary universe,
> matching the Stacks quantifications.

```lean
def IsMittagLeffler (R : Type uR) [CommRing R] (M : Type uM)
    [AddCommGroup M] [Module R M] : Prop
```

## Tag 059G, a remark

[Tag 059G](https://stacks.math.columbia.edu/tag/059G) in the Stacks Project.

**`CategoryTheory.Functor.isMittagLefflerSystem_iff_isMittagLeffler_dual`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/MittagLeffler/Dual.lean, line 249](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/MittagLeffler/Dual.lean#L249). The attribute's comment: “The content is the reduction of criterion (4) of 059E to the single test module `R`, stated for finitely generated projective members and an arbitrary index category, and as an iff; the passage to the colimit is 059E and the system comes from 058G. See the module docstring.”.

> **Stacks 059G.** Let `R` be a commutative ring and let `F : J ⥤ ModuleCat R` be a diagram
> `(M i, f i j)` of finitely generated projective `R`-modules. Then `F` is a Mittag-Leffler system
> — that is, the inverse system of duals `(Hom_R(M i, N), Hom_R(f i j, N))` is Mittag-Leffler for
> every `R`-module `N`, and the `M i` are of finite presentation — if and only if the single
> inverse system of `R`-duals `(Hom_R(M i, R), Hom_R(f i j, R))` is Mittag-Leffler.
>
> Combined with criterion (4) of Proposition 059E, this says that for a flat module `M` written by
> Lazard's theorem (Theorem 058G) as the colimit of a directed system of finite free modules
> `M = colim M i`, it is enough for `(Hom_R(M i, R), Hom_R(f i j, R))` to be Mittag-Leffler for `M`
> to be a Mittag-Leffler module.

```lean
public theorem isMittagLefflerSystem_iff_isMittagLeffler_dual {R : Type u} [CommRing R]
    [Small.{v} R] {J : Type w} [Category.{w'} J] (F : J ⥤ ModuleCat.{v} R)
    [∀ i, Module.Finite R (F.obj i)] [∀ i, Module.Projective R (F.obj i)] :
    F.IsMittagLefflerSystem ↔
      (F.op ⋙ yoneda.obj (ModuleCat.of R (Shrink.{v} R))).IsMittagLeffler
```

## Tag 05CN, a lemma

[Tag 05CN](https://stacks.math.columbia.edu/tag/05CN) in the Stacks Project.

**`Module.mittagLeffler_tensorProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/MittagLeffler/TensorProduct.lean, line 358](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/MittagLeffler/TensorProduct.lean#L358). The attribute's comment: “Mittag-Leffler is spelled out inline as condition (1) of 059E.”.

> **Stacks 05CN.** If `R` is a ring and `M`, `N` are Mittag-Leffler modules over `R`, then
> `M ⊗_R N` is a Mittag-Leffler module. The Mittag-Leffler condition is spelled out in the
> intrinsic form 059E (1): every map `f` from a finitely presented module into the module in
> question dominates and is dominated by a map `g` into a finitely presented module, domination
> meaning containment of the kernels of the maps `· ⊗ id_T`.

```lean
public theorem Module.mittagLeffler_tensorProduct {R : Type u} [CommRing R] [Small.{v} R]
    {M N : Type v} [AddCommGroup M] [Module R M] [AddCommGroup N] [Module R N]
    (hM : ∀ (P : Type v) [AddCommGroup P] [Module R P] [Module.FinitePresentation R P]
      (f : P →ₗ[R] M), ∃ (Q : Type v) (_ : AddCommGroup Q) (_ : Module R Q)
        (_ : Module.FinitePresentation R Q) (g : P →ₗ[R] Q), ∀ (T : Type v) [AddCommGroup T]
          [Module R T], LinearMap.ker (f.rTensor T) = LinearMap.ker (g.rTensor T))
    (hN : ∀ (P : Type v) [AddCommGroup P] [Module R P] [Module.FinitePresentation R P]
      (f : P →ₗ[R] N), ∃ (Q : Type v) (_ : AddCommGroup Q) (_ : Module R Q)
        (_ : Module.FinitePresentation R Q) (g : P →ₗ[R] Q), ∀ (T : Type v) [AddCommGroup T]
          [Module R T], LinearMap.ker (f.rTensor T) = LinearMap.ker (g.rTensor T)) :
    ∀ (P : Type v) [AddCommGroup P] [Module R P] [Module.FinitePresentation R P]
      (f : P →ₗ[R] M ⊗[R] N), ∃ (Q : Type v) (_ : AddCommGroup Q) (_ : Module R Q)
        (_ : Module.FinitePresentation R Q) (g : P →ₗ[R] Q), ∀ (T : Type v) [AddCommGroup T]
          [Module R T], LinearMap.ker (f.rTensor T) = LinearMap.ker (g.rTensor T)
```

## Tag 05CP, a lemma

[Tag 05CP](https://stacks.math.columbia.edu/tag/05CP) in the Stacks Project.

**`Module.mittagLeffler_iff_forall_finite_free`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/MittagLeffler/Criteria.lean, line 748](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/MittagLeffler/Criteria.lean#L748). The attribute's comment: “Mittag-Leffler is spelled out inline as condition (1) of 059E; domination as equality of the kernels of the tensored maps.”.

> **Stacks 05CP.** Let `R` be a ring and `M` an `R`-module. Then `M` is Mittag-Leffler if and
> only if for every finite free `R`-module `F` and every module map `f : F → M` there are a finitely
> presented `R`-module `Q` and a module map `g : F → Q` such that `f` and `g` dominate each other,
> that is `Ker(f ⊗ id_N) = Ker(g ⊗ id_N)` for every `R`-module `N`. Being Mittag-Leffler is spelled
> out in the intrinsic form 059E (1): the same condition with `F` ranging over all finitely
> presented modules.

```lean
public theorem Module.mittagLeffler_iff_forall_finite_free {R : Type u} [CommRing R] [Small.{v} R]
    {M : Type v} [AddCommGroup M] [Module R M] :
    (∀ (P : Type v) [AddCommGroup P] [Module R P] [Module.FinitePresentation R P]
        (f : P →ₗ[R] M), ∃ (Q : Type v) (_ : AddCommGroup Q) (_ : Module R Q)
          (_ : Module.FinitePresentation R Q) (g : P →ₗ[R] Q), ∀ (N : Type v) [AddCommGroup N]
            [Module R N], LinearMap.ker (f.rTensor N) = LinearMap.ker (g.rTensor N)) ↔
      ∀ (F : Type v) [AddCommGroup F] [Module R F] [Module.Free R F] [Module.Finite R F]
        (f : F →ₗ[R] M), ∃ (Q : Type v) (_ : AddCommGroup Q) (_ : Module R Q)
          (_ : Module.FinitePresentation R Q) (g : F →ₗ[R] Q), ∀ (N : Type v) [AddCommGroup N]
            [Module R N], LinearMap.ker (f.rTensor N) = LinearMap.ker (g.rTensor N)
```

## Tag 05CQ, a lemma

[Tag 05CQ](https://stacks.math.columbia.edu/tag/05CQ) in the Stacks Project.

**`Module.mittagLeffler_trans`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/MittagLeffler/RestrictScalars.lean, line 284](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/MittagLeffler/RestrictScalars.lean#L284). The attribute's comment: “Mittag-Leffler is spelled out inline as condition (1) of 059E.”.

> **Stacks 05CQ.** Let `R → S` be a ring map with `S` finitely presented as an `R`-module (for
> instance a finite and finitely presented ring map) and let `M` be an `S`-module. If `M` is
> Mittag-Leffler over `S` then `M` is Mittag-Leffler over `R`. The Mittag-Leffler condition is
> spelled out in the intrinsic form 059E (1): every map `f` from a finitely presented module into
> `M` dominates and is dominated by a map `g` into a finitely presented module, domination meaning
> containment of the kernels of the maps `· ⊗ id_N`.

```lean
public theorem Module.mittagLeffler_trans {R : Type u} {S : Type w} {M : Type v} [CommRing R]
    [CommRing S] [Algebra R S] [Small.{v} R] [Module.FinitePresentation R S] [AddCommGroup M]
    [Module R M] [Module S M] [IsScalarTower R S M]
    (hM : ∀ (P : Type v) [AddCommGroup P] [Module S P] [Module.FinitePresentation S P]
      (f : P →ₗ[S] M), ∃ (Q : Type v) (_ : AddCommGroup Q) (_ : Module S Q)
        (_ : Module.FinitePresentation S Q) (g : P →ₗ[S] Q), ∀ (N : Type v) [AddCommGroup N]
          [Module S N], LinearMap.ker (f.rTensor N) = LinearMap.ker (g.rTensor N)) :
    ∀ (P : Type v) [AddCommGroup P] [Module R P] [Module.FinitePresentation R P]
      (f : P →ₗ[R] M), ∃ (Q : Type v) (_ : AddCommGroup Q) (_ : Module R Q)
        (_ : Module.FinitePresentation R Q) (g : P →ₗ[R] Q), ∀ (N : Type v) [AddCommGroup N]
          [Module R N], LinearMap.ker (f.rTensor N) = LinearMap.ker (g.rTensor N)
```

## Tag 05CR, a lemma

[Tag 05CR](https://stacks.math.columbia.edu/tag/05CR) in the Stacks Project.

**`Module.mittagLeffler_restrictScalars_iff_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/MittagLeffler/Quotient.lean, line 293](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/MittagLeffler/Quotient.lean#L293). The attribute's comment: “Mittag-Leffler is spelled out inline as condition (1) of 059E; `S = R/I` with `I` finitely generated is spelled abstractly as a surjective `algebraMap R S` with `S` finitely presented as an `R`-module.”.

> **Stacks 05CR.** Let `R` be a ring and let `S = R/I` for a finitely generated ideal `I`,
> presented here as an `R`-algebra with surjective structure map which is finitely presented as an
> `R`-module. Let `M` be an `S`-module. Then `M` is a Mittag-Leffler module over `R` if and only if
> `M` is a Mittag-Leffler module over `S`. The Mittag-Leffler condition is spelled out in the
> intrinsic form 059E (1): every map `f` from a finitely presented module into `M` dominates and is
> dominated by a map `g` into a finitely presented module, domination meaning equality of the kernels
> of the maps `· ⊗ id_N`.

```lean
public theorem Module.mittagLeffler_restrictScalars_iff_of_surjective {R : Type u} {S : Type w}
    {M : Type v} [CommRing R] [CommRing S] [Algebra R S] [Small.{v} R]
    [Module.FinitePresentation R S] [AddCommGroup M] [Module R M] [Module S M]
    [IsScalarTower R S M] (hRS : Function.Surjective (algebraMap R S)) :
    (∀ (P : Type v) [AddCommGroup P] [Module R P] [Module.FinitePresentation R P]
      (f : P →ₗ[R] M), ∃ (Q : Type v) (_ : AddCommGroup Q) (_ : Module R Q)
        (_ : Module.FinitePresentation R Q) (g : P →ₗ[R] Q), ∀ (N : Type v) [AddCommGroup N]
          [Module R N], LinearMap.ker (f.rTensor N) = LinearMap.ker (g.rTensor N)) ↔
      ∀ (P : Type v) [AddCommGroup P] [Module S P] [Module.FinitePresentation S P]
        (f : P →ₗ[S] M), ∃ (Q : Type v) (_ : AddCommGroup Q) (_ : Module S Q)
          (_ : Module.FinitePresentation S Q) (g : P →ₗ[S] Q), ∀ (N : Type v) [AddCommGroup N]
            [Module S N], LinearMap.ker (f.rTensor N) = LinearMap.ker (g.rTensor N)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.88, Tag 0599](https://stacks.math.columbia.edu/tag/0599)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
