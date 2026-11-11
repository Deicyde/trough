---
declaration: theorem
origin: cited
lean: TauCeti.centralizer_range_permTensorActionAlgHom_eq_range_tensorPowerRep_asAlgebraHom, TauCeti.centralizer_span_range_map_const_eq_range_permTensorActionAlgHom, TauCeti.centralizer_range_permTensorAction_eq_range_tensorPowerRep_asAlgebraHom, TauCeti.centralizer_range_tensorPowerRep_eq_range_permTensorActionAlgHom, TauCeti.mem_range_permTensorActionAlgHom_iff_forall_commute, TauCeti.mem_range_permTensorActionAlgHom_iff_forall_commute_tensorPowerRep, TauCeti.mem_range_tensorPowerRep_asAlgebraHom_iff_forall_commute_permTensorAction, TauCeti.centralizer_range_tensorPowerRep_asAlgebraHom_eq_range_permTensorActionAlgHom
statement: formalized
proof: formalized
---

# Schur-Weyl duality: the commutant of the image of `k[S_d]` is the image of `k[GLₙ]`

```lean
TauCeti.centralizer_range_permTensorActionAlgHom_eq_range_tensorPowerRep_asAlgebraHom.{u_1}
  {k : Type u_1} {n d : ℕ} [Field k] [Infinite k] [NeZero ↑d.factorial] :
  Subalgebra.centralizer k (Set.range ⇑(TauCeti.permTensorActionAlgHom k n d)) =
    (TauCeti.tensorPowerRep k n d).asAlgebraHom.range
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The double centralizer theorem](../../ring-theory/part-01/semisimple/the-double-centralizer-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.centralizer_range_permTensorActionAlgHom_eq_range_tensorPowerRep_asAlgebraHom`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Symmetric/TensorAction/GeneralLinear.html#TauCeti.centralizer_range_permTensorActionAlgHom_eq_range_tensorPowerRep_asAlgebraHom).

## Other forms

**Schur-Weyl duality.** Formalized in Tau Ceti as [`TauCeti.centralizer_span_range_map_const_eq_range_permTensorActionAlgHom`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Symmetric/TensorAction/SchurWeyl.html#TauCeti.centralizer_span_range_map_const_eq_range_permTensorActionAlgHom).

```lean
TauCeti.centralizer_span_range_map_const_eq_range_permTensorActionAlgHom.{u_1} {k : Type u_1}
  {n d : ℕ} [Field k] [NeZero ↑d.factorial] :
  Subalgebra.centralizer k ↑(Submodule.span k (Set.range fun f => PiTensorProduct.map fun x => f)) =
    (TauCeti.permTensorActionAlgHom k n d).range
```

**Schur-Weyl duality for the group ranges.** Formalized in Tau Ceti as [`TauCeti.centralizer_range_permTensorAction_eq_range_tensorPowerRep_asAlgebraHom`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Symmetric/TensorAction/GeneralLinear.html#TauCeti.centralizer_range_permTensorAction_eq_range_tensorPowerRep_asAlgebraHom).

```lean
TauCeti.centralizer_range_permTensorAction_eq_range_tensorPowerRep_asAlgebraHom.{u_1} {k : Type u_1}
  {n d : ℕ} [Field k] [Infinite k] [NeZero ↑d.factorial] :
  Subalgebra.centralizer k (Set.range ⇑(TauCeti.permTensorAction k n d)) =
    (TauCeti.tensorPowerRep k n d).asAlgebraHom.range
```

**Schur-Weyl duality for the group ranges.** Formalized in Tau Ceti as [`TauCeti.centralizer_range_tensorPowerRep_eq_range_permTensorActionAlgHom`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Symmetric/TensorAction/GeneralLinear.html#TauCeti.centralizer_range_tensorPowerRep_eq_range_permTensorActionAlgHom).

```lean
TauCeti.centralizer_range_tensorPowerRep_eq_range_permTensorActionAlgHom.{u_1} {k : Type u_1}
  {n d : ℕ} [Field k] [Infinite k] [NeZero ↑d.factorial] :
  Subalgebra.centralizer k (Set.range ⇑(TauCeti.tensorPowerRep k n d)) =
    (TauCeti.permTensorActionAlgHom k n d).range
```

**Schur-Weyl duality, as a membership criterion.** Formalized in Tau Ceti as [`TauCeti.mem_range_permTensorActionAlgHom_iff_forall_commute`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Symmetric/TensorAction/SchurWeyl.html#TauCeti.mem_range_permTensorActionAlgHom_iff_forall_commute).

```lean
TauCeti.mem_range_permTensorActionAlgHom_iff_forall_commute.{u_1} {k : Type u_1} {n d : ℕ} [Field k]
  [NeZero ↑d.factorial] (x : Module.End k (PiTensorProduct k fun x => Fin n → k)) :
  x ∈ (TauCeti.permTensorActionAlgHom k n d).range ↔
    ∀ (f : (Fin n → k) →ₗ[k] Fin n → k), Commute x (PiTensorProduct.map fun x => f)
```

**Schur-Weyl duality, as a membership criterion.** Formalized in Tau Ceti as [`TauCeti.mem_range_permTensorActionAlgHom_iff_forall_commute_tensorPowerRep`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Symmetric/TensorAction/GeneralLinear.html#TauCeti.mem_range_permTensorActionAlgHom_iff_forall_commute_tensorPowerRep).

```lean
TauCeti.mem_range_permTensorActionAlgHom_iff_forall_commute_tensorPowerRep.{u_1} {k : Type u_1}
  {n d : ℕ} [Field k] [Infinite k] [NeZero ↑d.factorial]
  (x : Module.End k (PiTensorProduct k fun x => Fin n → k)) :
  x ∈ (TauCeti.permTensorActionAlgHom k n d).range ↔
    ∀ (g : GL (Fin n) k), Commute x ((TauCeti.tensorPowerRep k n d) g)
```

**Schur-Weyl duality, as a membership criterion.** Formalized in Tau Ceti as [`TauCeti.mem_range_tensorPowerRep_asAlgebraHom_iff_forall_commute_permTensorAction`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Symmetric/TensorAction/GeneralLinear.html#TauCeti.mem_range_tensorPowerRep_asAlgebraHom_iff_forall_commute_permTensorAction).

```lean
TauCeti.mem_range_tensorPowerRep_asAlgebraHom_iff_forall_commute_permTensorAction.{u_1}
  {k : Type u_1} {n d : ℕ} [Field k] [Infinite k] [NeZero ↑d.factorial]
  (x : Module.End k (PiTensorProduct k fun x => Fin n → k)) :
  x ∈ (TauCeti.tensorPowerRep k n d).asAlgebraHom.range ↔
    ∀ (σ : Equiv.Perm (Fin d)), Commute x ((TauCeti.permTensorAction k n d) σ)
```

**Schur-Weyl duality: the commutant of the image of `k[GLₙ]` is the image of `k[S_d]`.** Formalized in Tau Ceti as [`TauCeti.centralizer_range_tensorPowerRep_asAlgebraHom_eq_range_permTensorActionAlgHom`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Symmetric/TensorAction/GeneralLinear.html#TauCeti.centralizer_range_tensorPowerRep_asAlgebraHom_eq_range_permTensorActionAlgHom).

```lean
TauCeti.centralizer_range_tensorPowerRep_asAlgebraHom_eq_range_permTensorActionAlgHom.{u_1}
  {k : Type u_1} {n d : ℕ} [Field k] [Infinite k] [NeZero ↑d.factorial] :
  Subalgebra.centralizer k (Set.range ⇑(TauCeti.tensorPowerRep k n d).asAlgebraHom) =
    (TauCeti.permTensorActionAlgHom k n d).range
```

## Sources

- [Tau Ceti documentation: `TauCeti.centralizer_range_permTensorActionAlgHom_eq_range_tensorPowerRep_asAlgebraHom`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Symmetric/TensorAction/GeneralLinear.html#TauCeti.centralizer_range_permTensorActionAlgHom_eq_range_tensorPowerRep_asAlgebraHom)
- [Source of `TauCeti.centralizer_range_permTensorActionAlgHom_eq_range_tensorPowerRep_asAlgebraHom` in TauCeti/RepresentationTheory/Symmetric/TensorAction/GeneralLinear.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Symmetric/TensorAction/GeneralLinear.lean#L75)
