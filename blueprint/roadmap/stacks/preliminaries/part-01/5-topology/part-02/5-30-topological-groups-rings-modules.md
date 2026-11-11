---
declaration: section
origin: cited
lean: IsTopologicalGroup, ContinuousMonoidHom, mapTopology_nhds_hasBasis, continuous_action, continuous_iff_uncurry_continuous, continuous_comp, continuous_perm_inv, isTopologicalGroup_aut
statement: formalized
proof: formalized
---

# 5.30 Topological groups, rings, modules

Section 5.30 of the Stacks Project, [Tag 0B1Y](https://stacks.math.columbia.edu/tag/0B1Y). 12 tags here are carried by 19 declarations of the repository (all in StacksFrontier) and 12 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0B1Z, a definition

[Tag 0B1Z](https://stacks.math.columbia.edu/tag/0B1Z) in the Stacks Project.

Declarations registered for the tag:

- [`IsTopologicalGroup`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsTopologicalGroup#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Algebra/Group.lean, line 13](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/Group.lean#L13) (StacksFrontier): “a topological group”.
- [`ContinuousMonoidHom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ContinuousMonoidHom#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Algebra/Group.lean, line 14](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/Group.lean#L14) (StacksFrontier): “a homomorphism of topological groups”.

## Tag 0BMC, an example

[Tag 0BMC](https://stacks.math.columbia.edu/tag/0BMC) in the Stacks Project.

**`mapTopology_nhds_hasBasis`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AutomorphismGroup.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AutomorphismGroup.lean#L152).

> **Stacks 0BMC**.
> For every `f : E → E`, the family `{ U_S S f | S : Finset E }` of sets of maps agreeing with `f` on
> a finite subset `S` is a basis of neighbourhoods of `f` in the product (equivalently, when `E` is
> discrete, the compact-open) topology.

```lean
theorem mapTopology_nhds_hasBasis (f : E → E) :
    (nhds f).HasBasis (fun _ : Finset E => True) (fun S => U_S S f)
```

**`continuous_action`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AutomorphismGroup.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AutomorphismGroup.lean#L161).

> **Stacks 0BMC**.
> The action map `Map(E, E) × E → E`, `(f, e) ↦ f e`, is continuous when `E` carries the discrete
> topology and `Map(E, E) = (E → E)` carries the product (= compact-open) topology.

```lean
theorem continuous_action :
    Continuous (fun p : (E → E) × E => p.1 p.2)
```

**`continuous_iff_uncurry_continuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AutomorphismGroup.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AutomorphismGroup.lean#L169).

> **Stacks 0BMC**.
> A map `g : X → (E → E)` is continuous if and only if the uncurried map `X × E → E`,
> `(x, e) ↦ g x e`, is continuous.

```lean
theorem continuous_iff_uncurry_continuous
    {X : Type*} [TopologicalSpace X] (g : X → (E → E)) :
    Continuous g ↔ Continuous (fun p : X × E => g p.1 p.2)
```

**`continuous_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AutomorphismGroup.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AutomorphismGroup.lean#L178).

> **Stacks 0BMC**.
> Composition `Map(E, E) × Map(E, E) → Map(E, E)`, `(f, g) ↦ f ∘ g`, is continuous.

```lean
theorem continuous_comp :
    Continuous (fun p : (E → E) × (E → E) => p.1 ∘ p.2)
```

**`continuous_perm_inv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AutomorphismGroup.lean, line 198](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AutomorphismGroup.lean#L198).

> **Stacks 0BMC**.
> Inversion `σ ↦ σ⁻¹` on `Aut(E) = Equiv.Perm E` is continuous.

```lean
theorem continuous_perm_inv :
    Continuous (fun σ : Equiv.Perm E => σ⁻¹)
```

**`isTopologicalGroup_aut`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AutomorphismGroup.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AutomorphismGroup.lean#L206).

> **Stacks 0BMC**.
> `Aut(E) = Equiv.Perm E`, with the subspace topology induced from `Map(E, E)`, is a topological
> group.

```lean
theorem isTopologicalGroup_aut :
    IsTopologicalGroup (Equiv.Perm E)
```

## Tag 0B20, a lemma

[Tag 0B20](https://stacks.math.columbia.edu/tag/0B20) in the Stacks Project.

**`TopCat.hasLimits_grp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/GroupLimits.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/GroupLimits.lean#L46). The attribute's comment: “part (1): existence of limits”.

> **Stacks 0B20**, part (1). The category of topological groups has all small limits.
> This is Mathlib's `HasLimitsOfShape J (Grp C)`, obtained from the fact that
> `Grp.forget TopCat` creates limits.

```lean
theorem hasLimits_grp : HasLimits (Grp TopCat.{u})
```

**`TopCat.preservesLimits_grpForget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/GroupLimits.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/GroupLimits.lean#L52). The attribute's comment: “part (a): commutes with forgetful to TopCat”.

> **Stacks 0B20**, part (a). The forgetful functor from topological groups to topological
> spaces preserves all small limits; indeed Mathlib shows it creates them.

```lean
theorem preservesLimits_grpForget : PreservesLimits (Grp.forget TopCat.{u})
```

**`TopCat.preservesLimits_forgetGrp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/GroupLimits.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/GroupLimits.lean#L58). The attribute's comment: “part (b): commutes with forgetful to Grp”.

> **Stacks 0B20**, part (b). The forgetful functor from topological groups to groups
> preserves all small limits.

```lean
theorem preservesLimits_forgetGrp : PreservesLimits (forgetGrp.{u})
```

## Tag 0BR1, a lemma

[Tag 0BR1](https://stacks.math.columbia.edu/tag/0BR1) in the Stacks Project.

**`Stacks.Chapter05.Tag_0BR1.tfae_profinite_group`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/ProfiniteGroup.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/ProfiniteGroup.lean#L86). References: SGA 1 V (5.1); SGA 4 IV (2.7.2), “more general”.

> **Stacks 0BR1**.
> For a topological group `G`, the following are equivalent: `G` is profinite as a topological space;
> `G` is a limit of a diagram of finite discrete topological groups; `G` is a cofiltered limit of
> finite discrete topological groups.

```lean
theorem tfae_profinite_group (G : Type u) [Group G] [TopologicalSpace G]
    [IsTopologicalGroup G] :
    List.TFAE
      [ IsProfiniteTop G,
        IsLimitOfFiniteDiscreteGroups G,
        IsCofilteredLimitOfFiniteDiscreteGroups G ]
```

## Tag 0BR2, a definition

[Tag 0BR2](https://stacks.math.columbia.edu/tag/0BR2) in the Stacks Project.

Declarations registered for the tag:

- [`ProfiniteGrp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ProfiniteGrp#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Algebra/ProfiniteGroupCharacterization.lean, line 16](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/ProfiniteGroupCharacterization.lean#L16) (StacksFrontier): “a profinite group”. References: SGA 1 V (5.1); SGA 4 IV (2.7.2).
- [`ProfiniteGrp.of`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ProfiniteGrp.of#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Algebra/ProfiniteGroupCharacterization.lean, line 19](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/ProfiniteGroupCharacterization.lean#L19) (StacksFrontier): “the profinite group attached to a compact, Hausdorff, totally disconnected topological group”.

## Tag 0B21, a lemma

[Tag 0B21](https://stacks.math.columbia.edu/tag/0B21) in the Stacks Project.

**`TopGrp.forgetToGrpCat_preservesColimits`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/GroupColimits.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/GroupColimits.lean#L122). The attribute's comment: “commutation with the forgetful functor to groups”.

> **Stacks 0B21**, second part. Colimits of topological groups commute with the forgetful functor
> to the category of groups: the forgetful functor is a left adjoint, hence preserves colimits.

```lean
instance forgetToGrpCat_preservesColimits : PreservesColimits forgetToGrpCat.{u}
```

**`TopGrp.hasColimits`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/GroupColimits.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/GroupColimits.lean#L221). The attribute's comment: “existence of colimits”.

> **Stacks 0B21**, first part. The category of topological groups has colimits.

```lean
noncomputable instance hasColimits : HasColimits TopGrp.{u}
```

## Tag 0B22, a definition

[Tag 0B22](https://stacks.math.columbia.edu/tag/0B22) in the Stacks Project.

**`StacksTopologicalRing`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/Ring.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/Ring.lean#L65). References: EGA 0 (3.1.4).

> **Stacks 0B22**.
> A ring `R` equipped with a topology is a topological ring if addition
> $(x, y) \mapsto x + y$ and multiplication $(x, y) \mapsto x \cdot y$ are continuous as maps
> $R \times R \to R$.

```lean
def StacksTopologicalRing (R : Type*) [Ring R] [TopologicalSpace R] : Prop
```

**`StacksTopologicalRingHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/Ring.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/Ring.lean#L73). References: EGA 0 (20.3.1), “Hom. cont(A,B)”; EGA 0 (3.1.4); SGA 3 VIIB (0.1.3).

> **Stacks 0B22**.
> A bundled ring homomorphism `f : R →+* S` between topological rings is a homomorphism of
> topological rings if its underlying function is continuous.

```lean
def StacksTopologicalRingHom
    {R S : Type*} [Ring R] [Ring S] [TopologicalSpace R] [TopologicalSpace S]
    [IsTopologicalRing R] [IsTopologicalRing S]
    (f : R →+* S) : Prop
```

## Tag 0B23, a lemma

[Tag 0B23](https://stacks.math.columbia.edu/tag/0B23) in the Stacks Project.

**`TopCommRingCat.hasLimits`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/RingLimits.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/RingLimits.lean#L85). The attribute's comment: “existence of limits”.

> **Stacks 0B23.** The category of topological rings has all small limits.

```lean
instance hasLimits : HasLimits TopCommRingCat.{u}
```

**`TopCommRingCat.preservesLimits_forget₂TopCat`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/RingLimits.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/RingLimits.lean#L95). The attribute's comment: “part (a): commutes with forgetful to TopCat”.

> **Stacks 0B23**, part (a). The forgetful functor to topological spaces preserves all
> small limits: it carries `TopCommRingCat.limitCone` to `TopCat.limitCone`.

```lean
instance preservesLimits_forget₂TopCat :
    PreservesLimits (forget₂ TopCommRingCat.{u} TopCat.{u})
```

**`TopCommRingCat.preservesLimits_forget₂CommRingCat`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/RingLimits.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/RingLimits.lean#L108). The attribute's comment: “part (b): commutes with forgetful to CommRing”.

> **Stacks 0B23**, part (b). The forgetful functor to rings preserves all small limits:
> the image of `TopCommRingCat.limitCone` is the subring of sections of the underlying diagram
> of rings, which is a limit there for the same reason.

```lean
instance preservesLimits_forget₂CommRingCat :
    PreservesLimits (forget₂ TopCommRingCat.{u} CommRingCat.{u})
```

## Tag 0B24, a lemma

[Tag 0B24](https://stacks.math.columbia.edu/tag/0B24) in the Stacks Project.

**`TopCommRingCat.hasColimits`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/RingColimits.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/RingColimits.lean#L167). The attribute's comment: “part (1): existence of colimits”.

> **Stacks 0B24**, part (1). The category of topological rings has all small colimits.

```lean
noncomputable instance hasColimits : HasColimits TopCommRingCat.{u}
```

**`TopCommRingCat.preservesColimits_forget₂CommRingCat`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/RingColimits.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/RingColimits.lean#L175). The attribute's comment: “part (2): commutes with forgetful to CommRing”.

> **Stacks 0B24**, part (2). The forgetful functor from topological rings to rings preserves
> all small colimits, by the indiscrete-topology lift `TopCommRingCat.indiscreteCocone`.

```lean
noncomputable instance preservesColimits_forget₂CommRingCat :
    PreservesColimits (forget₂ TopCommRingCat.{u} CommRingCat.{u})
```

## Tag 0B25, a definition

[Tag 0B25](https://stacks.math.columbia.edu/tag/0B25) in the Stacks Project.

Declarations registered for the tag:

- [`TopModuleCat`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopModuleCat#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Algebra/Module.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/Module.lean#L52) (StacksFrontier): “(1), topological modules: the objects of this category are exactly the modules over a topological ring equipped with a topology making addition and scalar multiplication continuous. The `IsTopologicalAddGroup` field is no strengthening of the source: over a ring `-x = (-1) • x`, so continuity of negation follows from `ContinuousSMul`.”.
- [`TopModuleCat.of`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopModuleCat.of#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Algebra/Module.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/Module.lean#L57) (StacksFrontier): “(1), a topological module built from exactly the source's two conditions: `of` takes only `[ContinuousAdd M]` and `[ContinuousSMul R M]`, deriving `ContinuousNeg M` from `-x = (-1 : R) • x`.”.
- [`ContinuousLinearMap`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ContinuousLinearMap#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Algebra/Module.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/Module.lean#L61) (StacksFrontier): “(2), homomorphisms of topological modules: an `R`-linear map bundled with a proof that its underlying function is continuous.”. References: EGA 0 (18.5.3), “partial”; EGA 0 (19.1.1); SGA 3 VIIB (0.2); SGA 3 VIIB (0.2.2); SGA 3 VIIB (0.3.6); SGA 3 VIIB (0.5.B); SGA 3 VIIB (1.3.5.A); SGA 6 II (AppII.3.0.2).

## Tag 0B26, a lemma

[Tag 0B26](https://stacks.math.columbia.edu/tag/0B26) in the Stacks Project.

Declarations registered for the tag:

- [`TopModuleCat.instHasLimits`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopModuleCat.instHasLimits#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Algebra/ModuleLimits.lean, line 22](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/ModuleLimits.lean#L22) (StacksFrontier): “the category of topological modules has limits”.
- [`TopModuleCat.isLimit`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopModuleCat.isLimit#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Algebra/ModuleLimits.lean, line 23](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/ModuleLimits.lean#L23) (StacksFrontier): “limits are computed on the underlying modules”.
- [`TopModuleCat.instPreservesLimitsTopCatForget₂ContinuousLinearMapIdCarrierContinuousMapCarrier`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopModuleCat.instPreservesLimitsTopCatForget₂ContinuousLinearMapIdCarrierContinuousMapCarrier#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Algebra/ModuleLimits.lean, line 24](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/ModuleLimits.lean#L24) (StacksFrontier): “the forgetful functor to topological spaces preserves limits”.

## Tag 0B27, a lemma

[Tag 0B27](https://stacks.math.columbia.edu/tag/0B27) in the Stacks Project.

Declarations registered for the tag:

- [`TopModuleCat.instHasColimits`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopModuleCat.instHasColimits#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Algebra/ModuleColimits.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/ModuleColimits.lean#L49) (StacksFrontier): “existence of colimits”.
- [`TopModuleCat.isColimit`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopModuleCat.isColimit#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Algebra/ModuleColimits.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/ModuleColimits.lean#L50) (StacksFrontier): “compatibility with the forgetful functor: a colimit cocone on the underlying `R`-modules, given the coinduced topology, is a colimit cocone of topological `R`-modules”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 5.30, Tag 0B1Y](https://stacks.math.columbia.edu/tag/0B1Y)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
