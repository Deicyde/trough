# Boxes

- [box](def-box.md)

The tree walk only uses the points of a box; the leaf tests use the normalized coordinates, so that every polynomial below is bounded on the same cube $[-1,1]^5$.

- [bad](def-bad.md)

The certificate is a binary tree for each root box. Each internal node halves the box along one coordinate; each leaf is either a *gap leaf*, which shows that no point of the box gives a Rupert pair, or a *domain leaf*, which shows that no point of the box is reduced.
