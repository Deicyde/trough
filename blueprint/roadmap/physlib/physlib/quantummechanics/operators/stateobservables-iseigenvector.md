---
declaration: module
origin: cited
lean: LinearPMap.IsEigenvector, LinearPMap.IsEigenvector.apply_eq, LinearPMap.IsEigenvector.ne_zero
statement: formalized
proof: formalized
---

# Eigenvectors of partial linear maps

The module `Physlib.QuantumMechanics.Operators.StateObservables.IsEigenvector`, [Physlib/QuantumMechanics/Operators/StateObservables/IsEigenvector.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/StateObservables/IsEigenvector.lean): 3 declarations, 3 with a docstring.

## Main definitions

> - `LinearPMap.IsEigenvector`: a nonzero domain vector satisfying `T ψ = μ • ψ`.

**`LinearPMap.IsEigenvector`**, a def, [line 26](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/StateObservables/IsEigenvector.lean#L26).

> A nonzero vector in the domain of `T` satisfying `T ψ = μ • ψ`.

```lean
def IsEigenvector (T : H →ₗ.[ℂ] H) (ψ : T.domain) (μ : ℂ) : Prop
```

**`LinearPMap.IsEigenvector.apply_eq`**, a lemma, [line 30](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/StateObservables/IsEigenvector.lean#L30).

> The eigenvalue equation for a partial-map eigenvector.

```lean
lemma IsEigenvector.apply_eq {T : H →ₗ.[ℂ] H} {ψ : T.domain} {μ : ℂ}
    (hψ : T.IsEigenvector ψ μ) :
    T ψ = μ • (ψ : H)
```

**`LinearPMap.IsEigenvector.ne_zero`**, a lemma, [line 36](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/StateObservables/IsEigenvector.lean#L36).

> A partial-map eigenvector is nonzero.

```lean
lemma IsEigenvector.ne_zero {T : H →ₗ.[ℂ] H} {ψ : T.domain} {μ : ℂ}
    (hψ : T.IsEigenvector ψ μ) :
    (ψ : H) ≠ 0
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/QuantumMechanics/Operators/StateObservables/IsEigenvector.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/StateObservables/IsEigenvector.lean)
