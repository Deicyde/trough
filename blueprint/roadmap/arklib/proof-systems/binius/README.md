# Binius

This section documents the binary tower fields underlying the Binius commitment scheme protocols. Their hierarchical structure enables highly efficient arithmetic. ArkLib formalizes Binary Basefold (`ArkLib/ProofSystem/Binius/BinaryBasefold`) and the Binius ring-switching frontend composed with a separate Binary Basefold opening (`ArkLib/ProofSystem/Binius/FRIBinius`); Section [Ring Switching](../ring-switching/README.md) states that composition. The fused FRI-Binius protocol is not part of this coverage; `ROADMAP.md` records its status. This chapter does not describe the protocols further.

## Binary Tower Fields

We define the binary tower fields ([Diamond and Posen 2025](https://doi.org/10.1007/978-3-031-91134-7_4)) as defined originally as iterated quadratic extensions by Wie88([Wiedemann 1988](https://doi.org/10.1080/00150517.1988.12429608)). These fields, denoted $(\mathcal{T})_{\iota \in \mathbb{N}}$, provide a chain of nested field extensions for efficient arithmetic, particularly for operations involving subfields, by leveraging a highly compatible basis structure across the tower.

- [Binary Tower Field](def-binary-tower-field.md)
- [Irreducible defining polynomial](thm-binary-tower-field-irreducible.md)
- [Binary Tower Fields are fields](thm-binary-tower-fields-are-fields.md)

The structure of the tower provides a natural way to represent elements using a consistent set of variables. This leads to a family of multilinear bases that are compatible across different levels of the tower.

- [Computable Binary Tower Fields](def-computable-binary-tower-field.md)
