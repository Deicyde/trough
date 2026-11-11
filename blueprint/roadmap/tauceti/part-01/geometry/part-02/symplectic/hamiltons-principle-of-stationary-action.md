---
declaration: theorem
origin: cited
lean: TauCeti.isActionStationary_iff_eulerLagrange
statement: formalized
proof: formalized
---

# Hamilton's principle of stationary action

For `2 ≤ n ≤ ∞`, let `q` be `C^n` at every
point of `[a, b]` and let `L` be jointly `C²` along `q`. Then `q` is a stationary point of the
action of `L` among `C^n` variations with fixed endpoints between `a` and `b` exactly when it
solves the Euler–Lagrange equations `d/dt ∂_v L(t, q, q') = ∂_q L(t, q, q')` at every time strictly
between `a` and `b`.

```lean
TauCeti.isActionStationary_iff_eulerLagrange.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] {L : ℝ → E × E → ℝ} {a b : ℝ} {n : WithTop ℕ∞} {q : ℝ → E} (hn : 2 ≤ n)
  (hn' : n ≤ ↑⊤) (hq : ∀ t ∈ Set.uIcc a b, ContDiffAt ℝ n q t)
  (hL : ∀ t ∈ Set.uIcc a b, ContDiffAt ℝ 2 (Function.uncurry L) (t, q t, deriv q t)) :
  TauCeti.IsActionStationary n L q a b ↔
    ∀ t ∈ Set.uIoo a b,
      HasDerivAt (fun s => fderiv ℝ (fun u => L s (q s, u)) (deriv q s))
        (fderiv ℝ (fun y => L t (y, deriv q t)) (q t)) t
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.isActionStationary_iff_eulerLagrange`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Hamiltonian/LagrangianAction.html#TauCeti.isActionStationary_iff_eulerLagrange).

## Sources

- [Tau Ceti documentation: `TauCeti.isActionStationary_iff_eulerLagrange`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Hamiltonian/LagrangianAction.html#TauCeti.isActionStationary_iff_eulerLagrange)
- [Source of `TauCeti.isActionStationary_iff_eulerLagrange` in TauCeti/Geometry/Symplectic/Hamiltonian/LagrangianAction.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Symplectic/Hamiltonian/LagrangianAction.lean#L403)
