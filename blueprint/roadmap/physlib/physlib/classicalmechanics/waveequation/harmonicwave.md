---
declaration: module
origin: cited
lean: ClassicalMechanics.WaveVector, ClassicalMechanics.WaveVector.toDirection, ClassicalMechanics.harmonicWave, ClassicalMechanics.transverseHarmonicPlaneWave, ClassicalMechanics.transverseHarmonicPlaneWave_eq_planeWave
statement: formalized
proof: formalized
---

# Harmonic Wave

The module `Physlib.ClassicalMechanics.WaveEquation.HarmonicWave`, [Physlib/ClassicalMechanics/WaveEquation/HarmonicWave.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/WaveEquation/HarmonicWave.lean): 5 declarations, 5 with a docstring.

> Time-harmonic waves.
>
> …

**`ClassicalMechanics.WaveVector`**, an abbrev, [line 26](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/WaveEquation/HarmonicWave.lean#L26).

> The wavevector which indicates a direction and has magnitude `2π/λ`.

```lean
abbrev WaveVector (d : ℕ := 3)
```

**`ClassicalMechanics.WaveVector.toDirection`**, a def, [line 29](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/WaveEquation/HarmonicWave.lean#L29).

> Direction of a wavevector.

```lean
noncomputable def WaveVector.toDirection {d : ℕ} (k : WaveVector d) (h : k ≠ 0) :
    Direction d
```

**`ClassicalMechanics.harmonicWave`**, a def, [line 37](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/WaveEquation/HarmonicWave.lean#L37).

> General form of time-harmonic wave in terms of angular frequency `ω` and wave vector `k`.

```lean
noncomputable def harmonicWave (a g : ℝ → Space d → ℝ) (ω : WaveVector d → ℝ) (k : WaveVector d) :
    Time → Space d → ℝ
```

**`ClassicalMechanics.transverseHarmonicPlaneWave`**, a def, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/WaveEquation/HarmonicWave.lean#L49).

> Transverse monochromatic time-harmonic plane wave where the direction of propagation
> is taken to be `EuclideanSpace.single 2 1`. `f₀x` and `f₀y` are the respective amplitudes,
> `ω` is the angular frequency, `δx` and `δy` are the respective phases for `fx` and `fy`.

```lean
noncomputable def transverseHarmonicPlaneWave (k : WaveVector) (f₀x f₀y ω δx δy : ℝ)
    (hk : k = EuclideanSpace.single 2 (ω/c)) :
    Time → Space → EuclideanSpace ℝ (Fin 3)
```

**`ClassicalMechanics.transverseHarmonicPlaneWave_eq_planeWave`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/WaveEquation/HarmonicWave.lean#L58).

> The transverse harmonic planewave representation is equivalent to the general planewave
> expression with `‖k‖ = ω/c`.

```lean
lemma transverseHarmonicPlaneWave_eq_planeWave {c : ℝ} {k : WaveVector} {f₀x f₀y ω δx δy : ℝ}
    (hc_ge_zero : 0 < c) (hω_ge_zero : 0 < ω) (hk : k = EuclideanSpace.single 2 (ω/c)) :
    (transverseHarmonicPlaneWave k f₀x f₀y ω δx δy hk) = planeWave
    (fun p => (f₀x * Real.cos (-(ω/c)*p + δx)) • (EuclideanSpace.single 0 1) +
    (f₀y * Real.cos (-(ω/c)*p + δy)) • (EuclideanSpace.single 1 1)) c
    (WaveVector.toDirection k (by rw [hk]; simp [ne_of_gt, hc_ge_zero, hω_ge_zero]))
```

## Depends on

- [Wave equation](basic.md)

## Sources

- [Physlib/ClassicalMechanics/WaveEquation/HarmonicWave.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/WaveEquation/HarmonicWave.lean)
