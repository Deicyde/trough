---
declaration: section
origin: cited
lean: Module.IsCoherent, IsCoherentRing, IsBezout.instIsCoherentRing, ValuationRing.isCoherentRing, isCoherent_of_fg_submodule, finite_ker_and_coherent_range_coker, coherent_ker_and_coker_of_coherent, isCoherent_two_out_of_three
statement: formalized
proof: formalized
---

# 10.90 Coherent rings

Section 10.90 of the Stacks Project, [Tag 05CU](https://stacks.math.columbia.edu/tag/05CU). 6 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05CV, a definition

[Tag 05CV](https://stacks.math.columbia.edu/tag/05CV) in the Stacks Project.

**`Module.IsCoherent`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Coherent/Basic.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Coherent/Basic.lean#L72). The attribute's comment: “(1) coherent module: finite, every f.g. submodule finitely presented”. References: SGA 6 I (3.1), “special case”; SGA 6 IV (2.1), “special case”.

> An `R`-module `M` is *coherent* if it is finitely generated and every
> finitely generated submodule of `M` is finitely presented over `R`.

```lean
class Module.IsCoherent (R : Type*) (M : Type*) [Ring R] [AddCommGroup M] [Module R M] :
    Prop
```

**`IsCoherentRing`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Coherent/Basic.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Coherent/Basic.lean#L84). The attribute's comment: “(2) coherent ring: coherent as a module over itself”. References: EGA 0 (5.3.7), “special case”.

> A ring `R` is a *coherent ring* if it is coherent as a module over itself.

```lean
class IsCoherentRing (R : Type*) [Ring R] : Prop
```

## Tag 0EWV, an example

[Tag 0EWV](https://stacks.math.columbia.edu/tag/0EWV) in the Stacks Project.

**`IsBezout.instIsCoherentRing`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Coherent/Bezout.lean, line 138](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Coherent/Bezout.lean#L138). The attribute's comment: “Generalization from valuation rings to Bézout domains: the source's proof uses that finitely generated ideals are principal and that the ring is a domain, not that it is local. The source's valuation ring statement is `ValuationRing.isCoherentRing`.”.

> A Bézout domain is a coherent ring: a finitely generated ideal is principal
> (`IsBezout.isPrincipal_of_FG`), hence free since the ring is a domain, hence finitely presented.
> The source states this for a valuation ring, which is a local Bézout domain
> (`ValuationRing.iff_local_bezout_domain`); locality is not used.

```lean
public instance IsBezout.instIsCoherentRing (A : Type*) [CommRing A] [IsDomain A] [IsBezout A] :
    IsCoherentRing A
```

**`ValuationRing.isCoherentRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Coherent/Bezout.lean, line 146](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Coherent/Bezout.lean#L146).

> **Stacks 0EWV.** A valuation ring is a coherent ring: every finitely generated ideal is
> principal (`ValuationRing.instIsBezout`, Stacks 090Q), hence free as a valuation ring is a domain,
> hence finitely presented. This is the Bézout case `IsBezout.instIsCoherentRing`.

```lean
public theorem ValuationRing.isCoherentRing (A : Type*) [CommRing A] [IsDomain A]
    [ValuationRing A] : IsCoherentRing A
```

## Tag 05CW, a lemma

[Tag 05CW](https://stacks.math.columbia.edu/tag/05CW) in the Stacks Project.

**`isCoherent_of_fg_submodule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Coherent/Basic.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Coherent/Basic.lean#L108). The attribute's comment: “(1)”. References: EGA 0 (5.3.2), “submodule clause, ring”; EGA 0 (5.3.4), “special case”.

> A finitely generated submodule of a coherent module is coherent.

```lean
theorem isCoherent_of_fg_submodule
    {R M : Type*} [Ring R] [AddCommGroup M] [Module R M] [Module.IsCoherent R M]
    (N : Submodule R M) (hN : N.FG) :
    Module.IsCoherent R N
```

**`finite_ker_and_coherent_range_coker`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Coherent/Basic.lean, line 160](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Coherent/Basic.lean#L160). The attribute's comment: “(2)”. References: EGA 0 (5.3.4), “special case”; SGA 6 I (3.3), “special case”; SGA 6 I (3.4), “partial”.

> If `φ : N → M` with `N` finite and `M` coherent, then the kernel of
> `φ` is finite, the range of `φ` is coherent, and the cokernel `M ⧸ range φ` is
> coherent.

```lean
theorem finite_ker_and_coherent_range_coker
    {R N M : Type*} [Ring R] [AddCommGroup N] [Module R N]
    [AddCommGroup M] [Module R M] [Module.Finite R N] [Module.IsCoherent R M]
    (φ : N →ₗ[R] M) :
    Module.Finite R (LinearMap.ker φ) ∧
      Module.IsCoherent R (LinearMap.range φ) ∧
      Module.IsCoherent R (M ⧸ LinearMap.range φ)
```

**`coherent_ker_and_coker_of_coherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Coherent/Basic.lean, line 182](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Coherent/Basic.lean#L182). The attribute's comment: “(3)”. References: EGA 0 (5.3.4), “special case”; SGA 6 I (3.3), “special case”; SGA 6 I (3.4), “partial”; SGA 6 IV (2.4), “partial”.

> If `φ : N → M` is a homomorphism of coherent modules, then its kernel
> and cokernel are coherent.

```lean
theorem coherent_ker_and_coker_of_coherent
    {R N M : Type*} [Ring R] [AddCommGroup N] [Module R N]
    [AddCommGroup M] [Module R M] [Module.IsCoherent R N] [Module.IsCoherent R M]
    (φ : N →ₗ[R] M) :
    Module.IsCoherent R (LinearMap.ker φ) ∧
      Module.IsCoherent R (M ⧸ LinearMap.range φ)
```

**`isCoherent_two_out_of_three`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Coherent/Basic.lean, line 246](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Coherent/Basic.lean#L246). The attribute's comment: “(4)”. References: SGA 6 I (3.3), “special case”; SGA 6 I (3.4), “special case”.

> Two-out-of-three for coherence in a short exact sequence `0 → M₁ → M₂ → M₃ → 0`, where `i` is
> injective, `p` is surjective and `range i = ker p`: any two of `M₁`, `M₂`, `M₃` coherent imply
> the third is coherent.

```lean
theorem isCoherent_two_out_of_three
    {R M₁ M₂ M₃ : Type*} [Ring R]
    [AddCommGroup M₁] [Module R M₁] [AddCommGroup M₂] [Module R M₂]
    [AddCommGroup M₃] [Module R M₃]
    (i : M₁ →ₗ[R] M₂) (p : M₂ →ₗ[R] M₃)
    (hi : Function.Injective i) (hp : Function.Surjective p)
    (hexact : LinearMap.range i = LinearMap.ker p) :
    (Module.IsCoherent R M₁ → Module.IsCoherent R M₂ → Module.IsCoherent R M₃) ∧
    (Module.IsCoherent R M₁ → Module.IsCoherent R M₃ → Module.IsCoherent R M₂) ∧
    (Module.IsCoherent R M₂ → Module.IsCoherent R M₃ → Module.IsCoherent R M₁)
```

## Tag 05CX, a lemma

[Tag 05CX](https://stacks.math.columbia.edu/tag/05CX) in the Stacks Project.

**`coherent_iff_finitePresentation_of_coherentRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Coherent/Basic.lean, line 328](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Coherent/Basic.lean#L328). References: SGA 6 I (3.5), “a) (i)⇔(ii)”.

> If `R` is a coherent ring, then an `R`-module `M` is coherent if and only if
> it is finitely presented.

```lean
theorem coherent_iff_finitePresentation_of_coherentRing
    (hR : Module.IsCoherent R R)
    (M : Type*) [AddCommGroup M] [Module R M] :
    Module.IsCoherent R M ↔ Module.FinitePresentation R M
```

## Tag 05CY, a lemma

[Tag 05CY](https://stacks.math.columbia.edu/tag/05CY) in the Stacks Project.

**`isCoherentRing_of_isNoetherianRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Coherent/Basic.lean, line 345](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Coherent/Basic.lean#L345). References: SGA 6 I (3.6), “special case”.

> Every left Noetherian ring is a coherent ring.

```lean
theorem isCoherentRing_of_isNoetherianRing (R : Type*) [Ring R] [IsNoetherianRing R] :
    IsCoherentRing R
```

## Tag 05CZ, a proposition

[Tag 05CZ](https://stacks.math.columbia.edu/tag/05CZ) in the Stacks Project.

**`IsCoherentRing.tfae_flat_pi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Coherent/Flat.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Coherent/Flat.lean#L137). The attribute's comment: “Test data in the universe of `R`. See the module docstring.”.

> **Stacks 05CZ** (Chase's theorem). Let `R` be a commutative ring. The following are
> equivalent: (1) `R` is coherent; (2) any product of flat `R`-modules is flat; (3) for every set
> `A` the module `R^A` is flat.

```lean
theorem IsCoherentRing.tfae_flat_pi (R : Type u) [CommRing R] :
    List.TFAE
      [IsCoherentRing R,
        ∀ (A : Type u) (Q : A → Type u) [∀ α, AddCommGroup (Q α)] [∀ α, Module R (Q α)],
          (∀ α, Module.Flat R (Q α)) → Module.Flat R (∀ α, Q α),
        ∀ A : Type u, Module.Flat R (A → R)]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.90, Tag 05CU](https://stacks.math.columbia.edu/tag/05CU)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
