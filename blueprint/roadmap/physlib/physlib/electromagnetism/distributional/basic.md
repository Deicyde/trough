---
declaration: module
origin: cited
lean: Electromagnetism.DistElectromagneticPotential, Electromagnetism.DistElectromagneticPotential.valEquiv, Electromagnetism.DistElectromagneticPotential.valLinearEquiv, Electromagnetism.DistElectromagneticPotential.ofFunction
statement: formalized
proof: formalized
---

# The Electromagnetic Potential

The module `Physlib.Electromagnetism.Distributional.Basic`, [Physlib/Electromagnetism/Distributional/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Distributional/Basic.lean): 6 declarations (2 instances with no name), 4 with a docstring.

## i. Overview

> The electromagnetic potential `A^μ` is the fundamental objects in
> electromagnetism. Mathematically it is related to a connection
> on a `U(1)`-bundle.
>
> We define the electromagnetic potential as a distribution from
> spacetime to contravariant Lorentz vectors. The notation "𝓓'(Ω, F)" is used for the
> space of `F`-valued distributions on the open set `Ω`. It is also worth noting here that this
> definition of distribution is over the reals ℝ.

## ii. Key results

> - `DistElectromagneticPotential` : the type of electromagnetic potentials as distributions.

## iv. References

> * https://www.dpmms.cam.ac.uk/~cmw50/resources/M3P18/M3P18Ch2.pdf [ref: cambridge\_m3p18\_ch2]
> * L. Schwartz, Théorie des distributions [ref: schwartz1950]

## A. The electromagnetic potential as a distribution

**`Electromagnetism.DistElectromagneticPotential`**, a structure, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Distributional/Basic.lean#L60).

> The electromagnetic potential as a distribution and as a tensor `A^μ`.

```lean
structure DistElectromagneticPotential (d : ℕ := 3) where
  /-- The underlying spacetime distribution. -/
  val : 𝓓'(⟨Set.univ (α := SpaceTime d), isOpen_univ⟩, Lorentz.Vector d)
```

### A.1. Equivalence to distributions

**`Electromagnetism.DistElectromagneticPotential.valEquiv`**, a def, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Distributional/Basic.lean#L73).

> The equivalence between an electromagnetic potential and its underlying distribution.

```lean
def valEquiv {d : ℕ} :
    DistElectromagneticPotential d ≃
      𝓓'(⟨Set.univ (α := SpaceTime d), isOpen_univ⟩, Lorentz.Vector d)
```

**An instance with no name**, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Distributional/Basic.lean#L85).

```lean
noncomputable instance {d : ℕ} : AddCommGroup (DistElectromagneticPotential d)
```

**An instance with no name**, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Distributional/Basic.lean#L88).

```lean
noncomputable instance {d : ℕ} : Module ℝ (DistElectromagneticPotential d)
```

**`Electromagnetism.DistElectromagneticPotential.valLinearEquiv`**, a def, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Distributional/Basic.lean#L92).

> The linear equivalence between an electromagnetic potential and its underlying distribution.

```lean
noncomputable def valLinearEquiv {d : ℕ} :
    DistElectromagneticPotential d ≃ₗ[ℝ]
      𝓓'(⟨Set.univ (α := SpaceTime d), isOpen_univ⟩, Lorentz.Vector d)
```

## B. Functions as distributions

**`Electromagnetism.DistElectromagneticPotential.ofFunction`**, a def, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Distributional/Basic.lean#L104).

> The distribution induced by a spacetime function.

```lean
noncomputable def ofFunction {d} (f : SpaceTime d → Lorentz.Vector d) :
    DistElectromagneticPotential d
```

## Depends on

- [Spacetime](../../spaceandtime/spacetime/basic.md)

## Sources

- [Physlib/Electromagnetism/Distributional/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Distributional/Basic.lean)
