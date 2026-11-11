---
declaration: section
origin: cited
lean: MetaMathlibExt.IsDenseLinearOrderWithoutEndpoints
statement: formalized
proof: formalized
---

# Ordered sets: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Order/ordered-sets/index.html).

Partial, strict and total orders, dense linear orders, monotone maps and sequences, and representations of finite posets.

## Dense linear order without endpoints

A relation $R$ on a type $\alpha$ is a *dense linear
order without endpoints* if it is a strict total order (irreflexive, transitive, and
trichotomous: for all $a, b$, at least one of $R(a,b)$, $a = b$, $R(b,a)$ holds), it is dense
(whenever $R(a,b)$, there is $c$ with $R(a,c)$ and $R(c,b)$), and it has no endpoints (for every
$a$ there are $b$ and $b'$ with $R(b,a)$ and $R(a,b')$).

Formalized by `MetaMathlibExt.IsDenseLinearOrderWithoutEndpoints`, a definition declared in [MathlibExt/SetTheory/Order/DenseLinearOrder.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Order/DenseLinearOrder.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Order/ordered-sets/index.html#is-dense-linear-order-without-endpoints).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ordered sets](https://deicyde.github.io/atlas-lean/roadmap/Order/ordered-sets/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Order/ordered-sets)
