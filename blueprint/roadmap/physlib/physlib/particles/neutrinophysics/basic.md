---
declaration: module
origin: cited
lean: diagPhase, diagPhase_zero, diagPhase_zero_eq, diagPhase_star, diagPhase_mul, diagPhaseUnitary, diagPhaseShift_coe_matrix, leptonPhaseShift
statement: formalized
proof: formalized
---

# The PMNS matrix

The module `Physlib.Particles.NeutrinoPhysics.Basic`, [Physlib/Particles/NeutrinoPhysics/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/NeutrinoPhysics/Basic.lean): 14 declarations, 14 with a docstring.

> The definition the PMNS matrix, which describes neutrino oscillations as part of U(3).

**`diagPhase`**, a def, [line 26](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/NeutrinoPhysics/Basic.lean#L26).

> diagonal phase matrix from a real-valued function on indices

```lean
def diagPhase (θ : Fin 3 → ℝ) : Matrix (Fin 3) (Fin 3) ℂ
```

**`diagPhase_zero`**, a lemma, [line 31](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/NeutrinoPhysics/Basic.lean#L31).

> lemma stating that the diagonal phase matrix with all zeros is the identity matrix

```lean
lemma diagPhase_zero:
    diagPhase (fun _ : Fin 3 => 0) = 1
```

**`diagPhase_zero_eq`**, a lemma, [line 38](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/NeutrinoPhysics/Basic.lean#L38).

> lemma stating that diagPhase with θ = 0 is equal to diagPhase with all zero phases

```lean
lemma diagPhase_zero_eq : diagPhase 0 = diagPhase (fun _ : Fin 3 => 0)
```

**`diagPhase_star`**, a lemma, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/NeutrinoPhysics/Basic.lean#L45).

> lemma stating that the Hermitian conjugate of diagPhase diag(+iθ\_i)
> is just diagPhase with entries diag(-iθ\_i)

```lean
lemma diagPhase_star (θ : Fin 3 → ℝ) :
    (diagPhase θ)ᴴ = diagPhase (- θ)
```

**`diagPhase_mul`**, a lemma, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/NeutrinoPhysics/Basic.lean#L52).

> lemma stating that multiplying two phase matrices is equivalent to adding the phases

```lean
lemma diagPhase_mul (θ φ : Fin 3 → ℝ) :
    diagPhase θ * diagPhase φ = diagPhase (θ + φ)
```

**`diagPhaseUnitary`**, a def, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/NeutrinoPhysics/Basic.lean#L58).

> diagonal phase matrix diag(iθ\_i) is part of the unitary group

```lean
def diagPhaseUnitary (θ : Fin 3 → ℝ) : unitaryGroup (Fin 3) ℂ
```

**`diagPhaseShift_coe_matrix`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/NeutrinoPhysics/Basic.lean#L71).

> The underlying matrix of the phase-shift element of the unitary group is the
> phase-shift matrix.

```lean
lemma diagPhaseShift_coe_matrix (θ : Fin 3 → ℝ) : ↑(diagPhaseUnitary θ) = diagPhase θ
```

**`leptonPhaseShift`**, a def, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/NeutrinoPhysics/Basic.lean#L76).

> The Lepton phase shift matrix as a `3×3` complex matrix, given three reals `a b c`.
> This dictates the phase shift freedom of the charged lepton sector.

```lean
def leptonPhaseShift (a b c : ℝ) : Matrix (Fin 3) (Fin 3) ℂ
```

**`neutrinoPhaseShift`**, a def, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/NeutrinoPhysics/Basic.lean#L82).

> The neutrino phase shift matrix as a `3×3` complex matrix, given three reals `d e f`.
> This dictates the phase shift freedom of the neutrino sector (If neutrinos are Dirac).

```lean
def neutrinoPhaseShift (d e f : ℝ) : Matrix (Fin 3) (Fin 3) ℂ
```

**`majoranaPhaseMatrix`**, a def, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/NeutrinoPhysics/Basic.lean#L88).

> If neutrinos are Majorana particles, then the neutrino phase shift matrix is physical,
> and cannot be absorbed into the definition of the neutrino fields.

```lean
def majoranaPhaseMatrix (α1 α2 : ℝ) : Matrix (Fin 3) (Fin 3) ℂ
```

**`PMNSDiracEquivalence`**, a def, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/NeutrinoPhysics/Basic.lean#L92).

> The Dirac PMNS matrix equivalence relations

```lean
def PMNSDiracEquivalence (U V : unitaryGroup (Fin 3) ℂ) : Prop
```

**`PMNSDiracEquivalence_refl`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/NeutrinoPhysics/Basic.lean#L97).

> The relation `PMNSDiracEquivalence` is reflexive.

```lean
lemma PMNSDiracEquivalence_refl :
    ∀ U : unitaryGroup (Fin 3) ℂ, PMNSDiracEquivalence U U
```

**`PMNSDiracEquivalence_symm`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/NeutrinoPhysics/Basic.lean#L103).

> The relation `PMNSDiracEquivalence` is symmetric.

```lean
lemma PMNSDiracEquivalence_symm :
    ∀ U V : unitaryGroup (Fin 3) ℂ, PMNSDiracEquivalence U V → PMNSDiracEquivalence V U
```

**`PMNSDiracEquivalence_trans`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/NeutrinoPhysics/Basic.lean#L111).

> The relation `PMNSDiracEquivalence` is transitive.

```lean
lemma PMNSDiracEquivalence_trans {U V W : unitaryGroup (Fin 3) ℂ} :
    PMNSDiracEquivalence U V → PMNSDiracEquivalence V W → PMNSDiracEquivalence U W
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Particles/NeutrinoPhysics/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/NeutrinoPhysics/Basic.lean)
