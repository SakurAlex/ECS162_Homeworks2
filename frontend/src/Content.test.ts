import { describe, test, expect } from 'vitest'
import { render, screen } from '@testing-library/svelte'
import Content from './Content.svelte'

describe('Content component', () => {
  test('shows Loading... on initial render', () => {
    render(Content)
    // There should be at least one "Loading..." message
    expect(screen.getAllByText('Loading...').length).toBeGreaterThanOrEqual(1)
  })
})