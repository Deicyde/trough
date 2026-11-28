---
catalog: module
---

# Completeness of the De Morgan basis

`Cslib.Computability.Circuit.Boolean.Complexity`, in [Cslib/Computability/Circuit/Boolean/Complexity.lean](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Circuit/Boolean/Complexity.lean), by Samuel Schlesinger. It declares nothing public by name.

> Every Boolean function has a De Morgan circuit, by the Lupanov construction with no data
> bits, so the basis is complete and `complexity interpretation f` is the circuit complexity of
> `f` over it, for any number of outputs. This agrees with the standard measure of
> [Jukna, Chapter 1][Jukna2012] up to the counting of constants and negations; see
> `Cslib.Computability.Circuit.Boolean.Basic`.
>
> ## References
>
> * [Stasys Jukna, *Boolean Function Complexity: Advances and Frontiers*][Jukna2012]

## Depends on

- [Boolean circuits](basic.md)
- [Circuit complexity](../complexity.md)

## Proof depends on

- [Lupanov's block construction](lupanovconstruction.md)

## Sources

- [Cslib/Computability/Circuit/Boolean/Complexity.lean at 8b510d01](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Circuit/Boolean/Complexity.lean)
- [Declaration ledger](../../../../../sources/cslib/Cslib.Computability.Circuit.Boolean.Complexity.json)
