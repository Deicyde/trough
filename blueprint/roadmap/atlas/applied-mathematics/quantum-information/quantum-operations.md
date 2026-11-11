---
declaration: section
origin: cited
lean: MathlibExt.QuantumInformation.Finite.NoCloning.no_cloning_two_state
statement: formalized
proof: formalized
---

# Quantum operations and channels

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/QuantumInformation/quantum-operations/index.html).

Quantum operations and channels covers the physically allowed transformations of quantum states, such as isometries and completely positive maps, and impossibility results like the no-cloning theorem.

## No-cloning theorem for two states

Let $H$ be a complex inner product space and let
$\psi, \varphi, b \in H$ be unit vectors with $0 < |\langle \psi, \varphi \rangle| < 1$. Then there
is no $\mathbb{C}$-linear isometric isomorphism $U$ of $H \otimes_{\mathbb{C}} H$ onto itself with
$U(\psi \otimes b) = \psi \otimes \psi$ and $U(\varphi \otimes b) = \varphi \otimes \varphi$.

## Sources

- W. K. Wootters and W. H. Zurek, "A single quantum cannot be cloned", Nature 299 (1982), 802-803, DOI 10.1038/299802a0.

Formalized by `MathlibExt.QuantumInformation.Finite.NoCloning.no_cloning_two_state`, a theorem declared in [MathlibExt/QuantumInformation/Finite/NoCloning.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/QuantumInformation/Finite/NoCloning.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/QuantumInformation/quantum-operations/index.html#no-cloning-two-state).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Quantum operations and channels](https://deicyde.github.io/atlas-lean/roadmap/QuantumInformation/quantum-operations/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/QuantumInformation/quantum-operations)
