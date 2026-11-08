---
declaration: theorem
origin: cited
lean: RungeKuttaOrderConditions.Butcher.gauss_order6_rat
statement: formalized
proof: formalized
---

# Certified Runge-Kutta Order Conditions

> Certifies Runge-Kutta order conditions over planar rooted trees, including RK4 order four, Dormand-Prince order five, and Gauss-Legendre order six.

*Quoted from the card [LeanPool/projects/runge-kutta-order-conditions.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/runge-kutta-order-conditions.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 8 main results, each with its informal statement quoted from the card. The scan finds 8 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`RungeKuttaOrderConditions.Butcher.satisfiesOrderConditions_iff`](https://leanpool.github.io/lean-pool/LeanPool/RungeKuttaOrderConditions/ButcherOrder.html#RungeKuttaOrderConditions.Butcher.satisfiesOrderConditions_iff) (theorem), declared in [LeanPool/RungeKuttaOrderConditions/ButcherOrder.lean, line 453](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/RungeKuttaOrderConditions/ButcherOrder.lean#L453): “Reduces order-p Runge-Kutta conditions to a finite catalogue check over rooted trees.”
- [`RungeKuttaOrderConditions.Butcher.rk4_order4`](https://leanpool.github.io/lean-pool/LeanPool/RungeKuttaOrderConditions/ButcherOrder.html#RungeKuttaOrderConditions.Butcher.rk4_order4) (theorem), declared in [LeanPool/RungeKuttaOrderConditions/ButcherOrder.lean, line 462](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/RungeKuttaOrderConditions/ButcherOrder.lean#L462): “Certifies that classical RK4 satisfies all planar rooted-tree order conditions through order four.”
- [`RungeKuttaOrderConditions.Butcher.rk4_not_ord5`](https://leanpool.github.io/lean-pool/LeanPool/RungeKuttaOrderConditions/ButcherOrder.html#RungeKuttaOrderConditions.Butcher.rk4_not_ord5) (theorem), declared in [LeanPool/RungeKuttaOrderConditions/ButcherOrder.lean, line 342](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/RungeKuttaOrderConditions/ButcherOrder.lean#L342): “Shows that RK4 fails a fifth-order condition, pinning its order exactly.”
- [`RungeKuttaOrderConditions.Butcher.orderCond_node_perm`](https://leanpool.github.io/lean-pool/LeanPool/RungeKuttaOrderConditions/ButcherOrder.html#RungeKuttaOrderConditions.Butcher.orderCond_node_perm) (theorem), declared in [LeanPool/RungeKuttaOrderConditions/ButcherOrder.lean, line 531](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/RungeKuttaOrderConditions/ButcherOrder.lean#L531): “Proves order conditions are invariant under permutations of a node's children.”
- [`RungeKuttaOrderConditions.Butcher.dp_order5`](https://leanpool.github.io/lean-pool/LeanPool/RungeKuttaOrderConditions/ButcherOrder.html#RungeKuttaOrderConditions.Butcher.dp_order5) (theorem), declared in [LeanPool/RungeKuttaOrderConditions/ButcherOrder.lean, line 625](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/RungeKuttaOrderConditions/ButcherOrder.lean#L625): “Certifies the Dormand-Prince RK45 fifth-order tableau through order five.”
- [`RungeKuttaOrderConditions.Butcher.gauss_order4`](https://leanpool.github.io/lean-pool/LeanPool/RungeKuttaOrderConditions/ButcherOrder.html#RungeKuttaOrderConditions.Butcher.gauss_order4) (theorem), declared in [LeanPool/RungeKuttaOrderConditions/ButcherOrder.lean, line 777](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/RungeKuttaOrderConditions/ButcherOrder.lean#L777): “Certifies the Gauss-Legendre three-stage tableau through order four over Q(sqrt(15)).”
- [`RungeKuttaOrderConditions.Butcher.gauss_order6`](https://leanpool.github.io/lean-pool/LeanPool/RungeKuttaOrderConditions/ButcherOrder.html#RungeKuttaOrderConditions.Butcher.gauss_order6) (theorem), declared in [LeanPool/RungeKuttaOrderConditions/ButcherOrder.lean, line 839](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/RungeKuttaOrderConditions/ButcherOrder.lean#L839): “Certifies the denominator-cleared (360-scaled) integer Z(sqrt(15)) Gauss-Legendre tableau through order six, the scaled certificate feeding the homogeneity bridge.”
- [`RungeKuttaOrderConditions.Butcher.gauss_order6_rat`](https://leanpool.github.io/lean-pool/LeanPool/RungeKuttaOrderConditions/ButcherOrder.html#RungeKuttaOrderConditions.Butcher.gauss_order6_rat) (theorem; a main declaration), declared in [LeanPool/RungeKuttaOrderConditions/ButcherOrder.lean, line 1003](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/RungeKuttaOrderConditions/ButcherOrder.lean#L1003): “Certifies the Gauss-Legendre s=3 tableau through order six over Q(sqrt(15)), via the formalized homogeneity bridge from the 360-scaled integer certificate.”

## Project

- Authors: Carles Marín.
- Source: *What Order a Method Knows* by Carles Marín, [doi:10.5281/zenodo.20787666](https://doi.org/10.5281/zenodo.20787666).
- Project repository: [karlesmarin/runge-kutta-order-conditions-lean](https://github.com/karlesmarin/runge-kutta-order-conditions-lean).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 65L06, 65L05, 05C05.
- In Lean Pool: [LeanPool/RungeKuttaOrderConditions](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/RungeKuttaOrderConditions), from the card [LeanPool/projects/runge-kutta-order-conditions.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/runge-kutta-order-conditions.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/runge-kutta-order-conditions.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/runge-kutta-order-conditions.yaml)
- [Lean Pool at 2b205bf9: LeanPool/RungeKuttaOrderConditions](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/RungeKuttaOrderConditions)
