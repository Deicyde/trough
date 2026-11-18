---
catalog: module
---

# Completeness of the De Morgan basis

`Cslib.Computability.Circuit.Boolean.Complexity`, in [Cslib/Computability/Circuit/Boolean/Complexity.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Boolean/Complexity.lean), by Samuel Schlesinger. It declares nothing public by name.

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

- [Cslib/Computability/Circuit/Boolean/Complexity.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Boolean/Complexity.lean)
