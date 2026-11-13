---
declaration: section
origin: cited
lean: AlgebraicGeometry.RingedSpace, AlgebraicGeometry.PresheafedSpace.Hom, fSharp, ChartedSpace.locallyRingedSpaceMap, AlgebraicGeometry.PresheafedSpace.comp, AlgebraicGeometry.PresheafedSpace.comp_base, AlgebraicGeometry.PresheafedSpace.comp_c
statement: formalized
proof: formalized
---

# 6.25 Ringed spaces

Section 6.25 of the Stacks Project, [Tag 0090](https://stacks.math.columbia.edu/tag/0090). 3 tags here are carried by 1 declaration of the repository (in StacksFrontier) and 6 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0091, a definition

[Tag 0091](https://stacks.math.columbia.edu/tag/0091) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.RingedSpace`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.RingedSpace#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/RingedSpace/Basic.lean, line 26](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/RingedSpace/Basic.lean#L26) (StacksFrontier): “a ringed space: a topological space together with a sheaf of commutative rings on it”. References: EGA 0 (4.1.1), “ringed space def”; SGA 4 Vbis (1.3.1), “topological space case”; SGA 4 IV (11.1.1), “site of opens of a space”.
- [`AlgebraicGeometry.PresheafedSpace.Hom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.PresheafedSpace.Hom#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/RingedSpace/Basic.lean, line 31](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/RingedSpace/Basic.lean#L31) (StacksFrontier): “a morphism of ringed spaces: a continuous map `base` together with an `f`-map `c` of sheaves of rings”. References: EGA 0 (3.5.1); EGA 0 (4.1.1), “morphism definition”; EGA 0 (3.5.2), “category of pairs”.

## Tag 0092, an example

[Tag 0092](https://stacks.math.columbia.edu/tag/0092) in the Stacks Project.

**`fSharp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/RingedSpace/ContinuousFunctions.lean, line 43](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/RingedSpace/ContinuousFunctions.lean#L43). The attribute's comment: “continuous functions”.

> The natural $f$-map $f^\sharp : \mathcal{C}^0_Y \to f_*\mathcal{C}^0_X$
> associated to a continuous map $f : X \to Y$ between topological spaces, given on
> sections over an open $V \subseteq Y$ by precomposition with $f$:
> $h \mapsto h \circ f|_{f^{-1}(V)}$. This is the morphism asserted to exist in the
> Stacks example.

```lean
noncomputable def fSharp {X Y : TopCat.{0}} (f : X ⟶ Y) :
    presheafC0 Y ⟶
      (TopCat.Presheaf.pushforward (CommAlgCat ℝ) f).obj
        (presheafC0 X)
```

Declarations registered for the tag:

- [`ChartedSpace.locallyRingedSpaceMap`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ChartedSpace.locallyRingedSpaceMap#doc) registered with `add_to_stacks` in [StacksFrontier/Geometry/Manifold/Sheaf/LocallyRingedSpace.lean, line 19](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Geometry/Manifold/Sheaf/LocallyRingedSpace.lean#L19) (StacksFrontier): “smooth case: a smooth map `f : M → N` of `C^∞`-manifolds induces the morphism of (locally) ringed spaces `(M, C^∞_M) → (N, C^∞_N)` given by `h ↦ h ∘ f` on sections”.

## Tag 0093, a definition

[Tag 0093](https://stacks.math.columbia.edu/tag/0093) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.PresheafedSpace.comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.PresheafedSpace.comp#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/RingedSpace/Comp.lean, line 24](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/RingedSpace/Comp.lean#L24) (StacksFrontier): “the composition of two morphisms of ringed spaces”. References: EGA 0 (3.5.2); EGA 0 (4.1.1), “composition”.
- [`AlgebraicGeometry.PresheafedSpace.comp_base`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.PresheafedSpace.comp_base#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/RingedSpace/Comp.lean, line 28](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/RingedSpace/Comp.lean#L28) (StacksFrontier): “its base map is the composite continuous map”. References: EGA 0 (3.5.2), “partial”; EGA 0 (4.1.1), “psi''=psi'o psi”.
- [`AlgebraicGeometry.PresheafedSpace.comp_c`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.PresheafedSpace.comp_c#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/RingedSpace/Comp.lean, line 32](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/RingedSpace/Comp.lean#L32) (StacksFrontier): “its sharp map is `g^♯` followed by the pushforward of `f^♯` along `g`”. References: EGA 0 (4.1.1), “theta''=psi\_*(th)o th'”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 6.25, Tag 0090](https://stacks.math.columbia.edu/tag/0090)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
