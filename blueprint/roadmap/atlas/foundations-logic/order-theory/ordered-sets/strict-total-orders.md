---
declaration: section
origin: cited
lean: MathlibExt.Order.StrictTotalOrder, MathlibExt.Order.StrictTotalOrder.ext
statement: formalized
proof: formalized
---

# Strict total orders

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Order/ordered-sets/strict-total-orders/index.html).

## Strict total order

A strict total order on a type $\alpha$ consists of a binary
relation $<$ on $\alpha$ that is irreflexive (no $a < a$), transitive ($a < b$ and $b < c$
imply $a < c$) and total on distinct elements (if $a \ne b$, then $a < b$ or $b < a$). It
models strict preference.

Formalized by `MathlibExt.Order.StrictTotalOrder`, a structure declared in [MathlibExt/Order/StrictTotalOrder.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Order/StrictTotalOrder.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Order/ordered-sets/strict-total-orders/index.html#strict-total-order).

## Strict total orders are determined by their relation

Two strict total orders on a
type $\alpha$ with the same relation are equal.

Formalized by `MathlibExt.Order.StrictTotalOrder.ext`, a theorem declared in [MathlibExt/Order/StrictTotalOrder.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Order/StrictTotalOrder.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Order/ordered-sets/strict-total-orders/index.html#ext).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Strict total orders](https://deicyde.github.io/atlas-lean/roadmap/Order/ordered-sets/strict-total-orders/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Order/ordered-sets/strict-total-orders)
