---
declaration: lemma
origin: cited
lean: Cayley.Pack.exists_face
statement: formalized
proof: formalized
---

# exists_face

Every $r$ with $|r_i| \le R$ for all $i$ is $\rho\, c_f(s_0, s_1)$ for some face $f$, some $0 \le \rho \le R$ and some $|s_0|, |s_1| \le 1$.

## Depends on

- [faces](def-faces.md)

## Proof

Take $\rho = \max_i |r_i|$ and $f$ the face through $r / \rho$ (any face if $r = 0$).

## Lean

Formalized as [`Cayley.Pack.exists_face`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.exists_face).

## Sources

- [Noperthedron blueprint: chapters/reduction.tex, line 303](https://github.com/jcreedcmu/Noperthedron/blob/0143f65be7f59b3ac09b99debb9c37944a0a2f4b/blueprint/src/chapters/reduction.tex#L303)
